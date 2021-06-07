import re
import sqlite3
import sys
import uuid
import datetime
from docx import Document

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from random import choice

from about import Ui_aboutdialog
from dataclasses import Subject, Tree, Section, List, Task, SectionRecord, Variable, VarTable, WorkList
from dataclasses import TaskSet, TaskSetLine, Variants
from mainwindow import Ui_MainWindow
from section import Ui_section_edit_form
from subject import Ui_subject_edit_form
from task2work import Ui_add_task_to_work
from task_dialog import Ui_task_edit_form
from taskset import Ui_taskset_form
from save_work import Ui_save_work_form
from variants import Ui_variants_add_form


class AboutWindow(QtWidgets.QDialog, Ui_aboutdialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = Ui_aboutdialog()
        self.ui.setupUi(self)


class TaskWindow(QtWidgets.QDialog, Ui_task_edit_form):
    def __init__(self):
        super(TaskWindow, self).__init__()
        self.task_id = None
        self.current_var = None
        self.is_loading = False
        self.variables = []
        self.var_list_model = QStringListModel([])
        self.ui = Ui_task_edit_form()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.condition_edit.textChanged.connect(self.find_variables)
        self.ui.var_type.addItem("Текст")
        self.ui.var_type.addItem("Целое число")
        self.ui.var_type.addItem("Дробное число")
        self.ui.case_noun.addItem("Именительный")
        self.ui.case_noun.addItem("Родительный")
        self.ui.case_noun.addItem("Дательный")
        self.ui.case_noun.addItem("Винительный")
        self.ui.case_noun.addItem("Творительный")
        self.ui.case_noun.addItem("Предложный")
        self.ui.variables_lv.clicked.connect(self.change_current_var)
        self.ui.var_type.currentIndexChanged.connect(self.change_var_type)
        self.ui.var_example.textChanged.connect(self.change_var_example)
        self.ui.case_noun.currentIndexChanged.connect(self.change_var_case)
        self.ui.range_edit.textChanged.connect(self.change_var_range)
        self.ui.tabWidget.currentChanged.connect(self.change_tab)

    @QtCore.pyqtSlot("QModelIndex")
    def change_current_var(self, modelIndex):
        self.current_var = self.variables[modelIndex.row()]
        self.load_variables_data()

    def change_var_type(self):
        if self.is_loading:
            return
        data = self.current_var.get_values()
        data[2] = self.ui.var_type.currentIndex()
        self.current_var.load_data(data)

    def change_var_example(self):
        if self.is_loading:
            return
        data = self.current_var.get_values()
        data[3] = self.ui.var_example.text()
        self.current_var.load_data(data)

    def change_var_case(self):
        if self.is_loading:
            return
        data = self.current_var.get_values()
        data[4] = self.ui.case_noun.currentIndex()
        self.current_var.load_data(data)

    def change_var_range(self):
        if self.is_loading:
            return
        data = self.current_var.get_values()
        data[5] = self.ui.range_edit.toPlainText()
        self.current_var.load_data(data)

    def load_variables_data(self):
        data = self.current_var.get_values()
        self.is_loading = True
        self.ui.var_type.setCurrentIndex(data[2])
        self.ui.var_example.setText(data[3])
        self.ui.case_noun.setCurrentIndex(data[4])
        self.ui.range_edit.setPlainText(data[5])
        self.is_loading = False

    def change_tab(self):
        # print(self.ui.tabWidget.currentIndex())
        pass

    def find_variables(self):
        vars = sorted(list(set(re.findall(r"\{(.*?)\}", self.ui.condition_edit.toPlainText()))))
        i = 0
        while i < len(self.variables):
            if self.variables[i].name not in vars:
                # print(self.variables[i].name)
                self.variables.remove(self.variables[i])
            else:
                vars.remove(self.variables[i].name)
                i += 1
        for var in vars:
            self.variables.append(Variable(var, self.task_id))
        self.variables.sort(key=lambda x: x.name)
        vars = []
        for var in self.variables:
            vars.append(var.name)
        if len(vars) > 0:
            self.var_list_model = QStringListModel(vars)
            self.ui.variables_lv.setModel(self.var_list_model)
            self.ui.tabWidget.setTabEnabled(1, True)
            self.ui.tabWidget.setTabEnabled(2, True)
        else:
            self.ui.tabWidget.setTabEnabled(1, False)
            self.ui.tabWidget.setTabEnabled(2, False)

    def set_id(self, task_id):
        self.task_id = task_id


class SectionEditForm(QtWidgets.QDialog, Ui_section_edit_form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_section_edit_form()
        self.ui.setupUi(self)
        self.rec = SectionRecord()


class SubjectEditForm(QtWidgets.QDialog, Ui_subject_edit_form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_subject_edit_form()
        self.ui.setupUi(self)


class VariantsAddForm(QtWidgets.QDialog, Ui_variants_add_form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_variants_add_form()
        self.ui.setupUi(self)


class AddTaskToWorkForm(QtWidgets.QDialog, Ui_add_task_to_work):
    def __init__(self):
        super().__init__()
        self.ui = Ui_add_task_to_work()
        self.ui.setupUi(self)


class SaveWorkForm(QtWidgets.QDialog, Ui_save_work_form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_save_work_form()
        self.ui.setupUi(self)


class TaskSetForm(QtWidgets.QWidget, Ui_taskset_form):
    def __init__(self):
        super().__init__()
        self.cur = None
        self.con = None
        self.task_table = None
        self.var_table = None
        self.taskset_table = None
        self.taskset_line_table = None
        self.variants_table = None
        self.taskset_list = List()
        self.taskset_line_list = List()
        self.variants_list = List()
        self.current_taskset_id = None
        self.current_variant_id = None
        self.variants_wnd = VariantsAddForm()
        self.ui = Ui_taskset_form()
        self.ui.setupUi(self)
        self.ui.taskset_lv.clicked.connect(self.taskset_clicked_action)
        self.ui.add_variant.clicked.connect(self.add_variants_action)
        self.ui.tabWidget.currentChanged.connect(self.tab_change_action)
        self.ui.variants_lv.clicked.connect(self.variant_clicked_action)

    def tab_change_action(self):
        if self.ui.tabWidget.currentIndex() == 1:
            if self.current_taskset_id:
                if not self.variants_table:
                    self.variants_table = Variants(self.cur)
                var_list = self.variants_table.select_detail(self.current_taskset_id)
                if var_list:
                    self.ui.variants_lv.model = QStandardItemModel()
                    self.variants_list.rowCount = 0
                    for var in var_list:
                        self.variants_list.insert("Вариант №" + str(var[2]), var[0])
                    self.ui.variants_lv.setModel(self.variants_list.model)

    def add_variants_action(self):
        if self.current_taskset_id:
            self.variants_wnd.exec()
            if self.variants_wnd.accept:
                amount = self.variants_wnd.ui.amount_sb.value()
                if not self.variants_table:
                    self.variants_table = Variants(self.cur)
                for number_variant in range(1, amount + 1):
                    text_variant, text_key = self.generate_variant_and_key(self.current_taskset_id,
                                                                           number_variant)
                    self.variants_table.insert([self.current_taskset_id,
                                                number_variant, text_variant, text_key])
                self.con.commit()

    def generate_variant_and_key(self, taskset, number):
        if not self.taskset_line_table:
            self.taskset_line_table = TaskSetLine(self.cur)
        taskset_line_list = self.taskset_line_table.select_detail(taskset)
        num_task = 1
        text_variant = "Вариант №" + str(number)
        text_key = "Ключ к варианту №" + str(number)
        for row in taskset_line_list:
            task_id = row[2]
            amount = row[3]
            for _ in range(amount):
                condition, answer = self.generate_condition_and_answer(num_task, task_id)
                num_task += 1
                text_variant += "\n" + condition
                text_key += "\n" + answer
        return text_variant, text_key

    def generate_condition_and_answer(self, number, task_id):
        text_condition = "Задание № " + str(number)
        text_answer = ""
        if not self.task_table:
            self.task_table = Task(self.cur)
        if not self.var_table:
            self.var_table = VarTable(self.cur)
        task = self.task_table.select1(task_id)[0]
        condition = task[3]
        formula = task[4]
        var_list = self.var_table.select_detail(task_id)
        for var in var_list:
            var_name = '{' + var[2] + '}'
            if "range" in var[8]:
                var_value = str(choice(list(eval(var[8]))))
            elif var[8][0] == '[' and var[8][-1] == ']':
                var_value = str(choice(eval(var[8])))
            else:
                var_value = var[4]
            condition = condition.replace(var_name, var_value)
            formula = formula.replace(var_name, var_value)
        text_condition += "\n" + condition
        text_answer = str(number) + ")" + str(eval(formula))
        return text_condition, text_answer

    def taskset_clicked_action(self):
        index = self.ui.taskset_lv.selectedIndexes()[0]
        if index:
            item = index.model().itemFromIndex(index)
            self.current_taskset_id = item.db_id
            # self.connect(self.con, self.cur)
            temp_line_list = self.taskset_line_table.select_with_task_name(
                self.current_taskset_id)
            if temp_line_list:
                self.taskset_line_list.import_data(temp_line_list, 0, 1)
                self.ui.tasksetline_lv.model = QStandardItemModel()
                self.ui.tasksetline_lv.setModel(self.taskset_line_list.model)

    def variant_clicked_action(self):
        index = self.ui.variants_lv.selectedIndexes()[0]
        if not self.variants_table:
            self.variants_table = Variants(self.cur)
        if index:
            item = index.model().itemFromIndex(index)
            self.current_variant_id = item.db_id
            condition, answer = self.variants_table.get_data_by_id(self.current_variant_id)
            self.ui.content_brow.setText(condition)
            self.ui.key_brow.setText(answer)

    def connect(self, connection, cursor):
        if not self.con:
            self.con = connection
        if not self.cur:
            self.cur = cursor
        if not self.taskset_table:
            self.taskset_table = TaskSet(self.cur)
        temp_list = self.taskset_table.select_all()
        if temp_list:
            self.taskset_list.import_data(temp_list, 0, 1)
            if not self.current_taskset_id:
                self.current_taskset_id = temp_list[0][0]
            if not self.taskset_line_table:
                self.taskset_line_table = TaskSetLine(self.cur)
            self.ui.taskset_lv.model = QStandardItemModel()
            self.ui.taskset_lv.setModel(self.taskset_list.model)
            self.ui.taskset_lv.model.item(self.current_taskset_id)
            temp_line_list = self.taskset_line_table.select_with_task_name(
                    self.current_taskset_id)
            if temp_line_list:
                self.taskset_line_list.import_data(temp_line_list, 0, 1)
                self.ui.tasksetline_lv.model = QStandardItemModel()
                self.ui.tasksetline_lv.setModel(self.taskset_line_list.model)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вспомогательные окна
        self.error_dialog = QtWidgets.QErrorMessage()
        self.about = AboutWindow()
        self.task_wnd = TaskWindow()
        self.task_to_work_wnd = AddTaskToWorkForm()
        self.save_work_wnd = SaveWorkForm()
        self.task_set_wnd = TaskSetForm()

        # Локальные переменные
        self.db_file = None
        self.subject_list = None
        self.section_list = None
        self.work_task_list = None
        self.task_list = None
        self.taskset_list = None
        self.taskset_table = None
        self.taskset_line_table = None
        self.current_subject = None
        self.current_section = None
        self.current_task = None
        self.con = None
        self.cur = None

        # Инициализация интерфейса
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.exit_act.triggered.connect(self.exit_action)
        self.ui.about_act.triggered.connect(self.about_action)
        self.ui.open_act.triggered.connect(self.open_action)
        self.ui.section_tv.clicked.connect(self.section_clicked)
        self.ui.task_add.clicked.connect(self.task_insert_action)
        self.ui.task_del.clicked.connect(self.task_delete_action)
        self.ui.task_list_view.clicked.connect(self.task_clicked)
        self.ui.section_add.clicked.connect(self.section_add_action)
        self.ui.subject_cb.currentIndexChanged.connect(self.subject_changed)
        self.ui.subject_add.clicked.connect(self.subject_add_action)
        self.ui.add_task_to_work.clicked.connect(self.add_task_to_work_action)
        self.ui.create_work.clicked.connect(self.create_work_action)
        self.ui.works_list.clicked.connect(self.open_work_list_action)

    def add_task_to_work_action(self):
        if self.current_task:
            index = self.ui.task_list_view.selectedIndexes()[0]
            self.task_to_work_wnd.ui.task_name.setText(index.model().itemData(index)[0])
            self.task_to_work_wnd.exec()
            if self.task_to_work_wnd.accept:
                if not self.work_task_list:
                    self.work_task_list = WorkList()
                self.work_task_list.insert(index.model().itemData(index)[0],
                                           self.current_task,
                                           self.task_to_work_wnd.ui.task_amount.value())
            self.ui.task_in_work_list.model = QStandardItemModel()
            self.ui.task_in_work_list.setModel(self.work_task_list.model)

    def task_insert_action(self):
        uid = 'tmp' + str(uuid.uuid4())
        task_table = Task(self.cur)
        task_table.delete_tmp()
        self.con.commit()
        task_table.insert([self.current_section, uid, '', ''])
        self.con.commit()
        task_id = task_table.id_by_name(uid)[0][0]
        self.task_wnd.set_id(task_id)
        self.task_wnd.exec()
        if self.task_wnd.accept:
            task_table.update("name", self.task_wnd.ui.task_edit.text(), task_id)
            task_table.update("condition", self.task_wnd.ui.condition_edit.toPlainText(), task_id)
            task_table.update("formula", self.task_wnd.ui.formula_edit.toPlainText(), task_id)
            self.con.commit()
            if self.task_wnd.variables:
                var_table = VarTable(self.cur)
                for var in self.task_wnd.variables:
                    values = var.get_values()
                    var_table.insert(values)
                self.con.commit()
                self.section_clicked()
        else:
            task_table.delete_tmp()
            self.con.commit()
        self.load_data()

    def create_work_action(self):
        self.save_work_wnd.exec()
        if self.save_work_wnd.accept:
            if not self.taskset_table:
                self.taskset_table = TaskSet(self.cur)
            date_creation = str(datetime.datetime.now())
            self.taskset_table.insert([self.save_work_wnd.ui.work_name.text(), date_creation])
            self.con.commit()
            taskset_id = self.taskset_table.get_id_by_date(date_creation)
            if not self.taskset_line_table:
                self.taskset_line_table = TaskSetLine(self.cur)
            for i in range(self.work_task_list.model.rowCount()):
                item = self.work_task_list.model.item(i)
                self.taskset_line_table.insert([taskset_id, item.task_id, item.amount])
            self.con.commit()
            self.work_task_list.model.clear()
            self.open_work_list_action()

    def open_work_list_action(self):
        self.task_set_wnd.connect(self.con, self.cur)
        self.task_set_wnd.show()

    def task_delete_action(self):
        if self.current_task:
            answer = QMessageBox.question(self, 'Удаление задачи', "Вы действительно хотите удалить задачу",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if answer == QMessageBox.Yes:
                var_table = VarTable(self.cur)
                vars = var_table.select_detail(self.current_task)
                if vars:
                    var_table.delete_detail(self.current_task)
                task_table = Task(self.cur)
                task_table.delete(self.current_task)
                self.con.commit()
                self.section_clicked()

    def section_clicked(self):
        index = self.ui.section_tv.selectedIndexes()[0]
        if index:
            # self.statusBar().showMessage(str(index.model().itemFromIndex(index).get_id()))
            self.current_section = index.model().itemFromIndex(index).get_id()
            self.task_list = None
            task_table = Task(self.cur)
            task_table.delete_tmp()
            self.task_list = task_table.select_detail(self.current_section)
            self.ui.task_list_view.model = QStandardItemModel()
            task_list = List()
            if self.task_list:
                task_list.import_data(self.task_list, 0, 2)
            self.ui.task_list_view.setModel(task_list.model)
            self.ui.task_list_view.show()

    def task_clicked(self):
        index = self.ui.task_list_view.selectedIndexes()[0]
        self.current_task = index.model().itemFromIndex(index).db_id

    def subject_changed(self):
        for row in self.subject_list:
            if self.ui.subject_cb.currentText() == row[1]:
                self.current_subject = row[0]
                self.load_data()

    def exit_action(self):
        exit(0)

    def about_action(self):
        self.about.show()

    def connect(self):
        if self.con:
            return
        else:
            self.con = sqlite3.connect(self.db_file)
            self.cur = self.con.cursor()

    def load_data(self):
        self.connect()
        # Загрузка предметов и инициализация комбобокса с выбором предметов
        if not self.current_subject:
            subject_table = Subject(self.cur)
            self.subject_list = subject_table.select_all()
            self.ui.subject_cb.clear()
            if self.subject_list:
                for row in self.subject_list:
                    self.ui.subject_cb.addItem(row[1])
                    self.current_subject = self.subject_list[0][0]
        # Загрузка разделов и инициализация Treeview с деревом разделов
        if self.current_subject:
            section_table = Section(self.cur)
            self.section_list = section_table.select_detail(self.current_subject)
            section_tree = Tree()
            section_tree.import_data(self.section_list, 0, 2, 3)
            self.ui.section_tv.model = QStandardItemModel()
            self.ui.section_tv.setModel(section_tree.model)
            self.ui.section_tv.header().resizeSection(0, 250)
            self.ui.section_tv.expandAll()
        else:
            self.error_dialog.showMessage('Не выбран предмет')

        # Загрузка задач и инициализация Task_list_view

    def open_action(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Файлы БД (*.mtdb);;All Files (*)", options=options)
        if file_name:
            self.statusBar().showMessage('Открыт файл ' + file_name)
            self.db_file = file_name
            self.load_data()

    def section_add_action(self):
        section_edit = SectionEditForm()
        section_edit.exec()
        if section_edit.accept:
            section_table = Section(self.cur)
            if section_edit.ui.is_root.isChecked():
                section_table.insert([self.current_subject, -1,
                                      '"' + section_edit.ui.section_edit.text() + '"'])
                self.con.commit()
            else:
                section_table.insert([self.current_subject,
                                      self.current_section,
                                      '"' + section_edit.ui.section_edit.text() + '"'])
                self.con.commit()
        self.load_data()

    def subject_add_action(self):
        subject_edit = SubjectEditForm()
        subject_edit.exec()
        if subject_edit.accept:
            subject_table = Subject(self.cur)
            subject_table.insert(['"' + subject_edit.ui.name_edit.text() + '"'])
            self.con.commit()
        self.current_subject = None
        self.load_data()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
