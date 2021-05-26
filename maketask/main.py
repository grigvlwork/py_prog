import re
import sqlite3
import sys
import uuid

from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QFileDialog

from about import Ui_aboutdialog
from dataclasses import Subject, Tree, Section, List, Task, SectionRecord, Variable
from mainwindow import Ui_MainWindow
from section import Ui_section_edit_form
from subject import Ui_subject_edit_form
from task_dailog import Ui_task_edit_form


class AboutWindow(QtWidgets.QDialog, Ui_aboutdialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = Ui_aboutdialog()
        self.ui.setupUi(self)


class TaskWindow(QtWidgets.QDialog, Ui_task_edit_form):
    def __init__(self):
        super(TaskWindow, self).__init__()
        self.task_id = None
        self.variables = []
        self.ui = Ui_task_edit_form()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.condition_edit.textChanged.connect(self.find_variables)

    def find_variables(self):
        vars = re.findall(r"\{(.*?)\}", self.ui.condition_edit.toPlainText())
        if len(vars) > 0:
            self.ui.tabWidget.setTabEnabled(1, True)
            self.ui.tabWidget.setTabEnabled(2, True)
            self.variables = []
            for var in vars:
                self.variables.append(Variable())
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
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)


class SubjectEditForm(QtWidgets.QDialog, Ui_subject_edit_form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_subject_edit_form()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вспомогательные окна
        self.error_dialog = QtWidgets.QErrorMessage()
        self.about = AboutWindow()
        self.task_wnd = TaskWindow(uuid.uuid4())

        # Локальные переменные
        self.db_file = None
        self.subject_list = None
        self.section_list = None
        self.task_list = None
        self.current_subject = None
        self.current_section = None
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
        self.ui.section_add.clicked.connect(self.section_add_action)
        self.ui.subject_cb.currentIndexChanged.connect(self.subject_changed)
        self.ui.subject_add.clicked.connect(self.subject_add_action)

    def task_insert_action(self):
        uid = '"' + str(uuid.uuid4()) + '"'
        task_table = Task()
        task_table.insert([self.current_section, uid, '""'])
        self.con.commit()
        id = task_table.select_
        self.task_wnd.exec()

    def section_clicked(self):
        index = self.ui.section_tv.selectedIndexes()[0]
        if index:
            # self.statusBar().showMessage(str(index.model().itemFromIndex(index).get_id()))
            self.current_section = index.model().itemFromIndex(index).get_id()
            self.task_list = None
            task_table = Task(self.cur)
            self.task_list = task_table.select_detail(self.current_section)
            self.ui.task_list_view.model = QStandardItemModel()
            task_list = List()
            if self.task_list:
                task_list.import_data(self.task_list, 0, 2)
            self.ui.task_list_view.setModel(task_list.model)
            self.ui.task_list_view.show()

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
