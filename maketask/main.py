import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QFileDialog
from mainwindow import Ui_MainWindow
from about import Ui_aboutdialog
from dataclasses import Subject, Tree, Section


class AboutWindow(QtWidgets.QDialog, Ui_aboutdialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = Ui_aboutdialog()
        self.ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Вспомогательные окна
        self.error_dialog = QtWidgets.QErrorMessage()
        self.about = AboutWindow()

        # Локальные переменные
        self.db_file = None
        self.subject_list = None
        self.section_list = None
        self.task_list = None
        self.current_subject = None
        self.current_section = None

        # Инициализация интерфейса
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.exit_act.triggered.connect(self.exit_action)
        self.ui.about_act.triggered.connect(self.about_action)
        self.ui.open_act.triggered.connect(self.open_action)
        self.ui.section_tv.clicked.connect(self.section_clicked)

    def section_clicked(self):
        index = self.ui.section_tv.selectedIndexes()[0]
        if index:
            # self.statusBar().showMessage(str(index.model().itemFromIndex(index).get_id()))
            self.current_section = index.model().itemFromIndex(index).get_id()
            self.task_list = None
            section_table = Section(self.cursor())
            self.task_list = section_table.select_detail(self.current_section)


    def exit_action(self):
        exit(0)

    def about_action(self):
        self.about.show()

    def load_data(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        # Загрузка предметов и инициализация комбобокса с выбором предметов
        subject_table = Subject(cur)
        self.subject_list = subject_table.select_all()
        self.ui.subject_cb.clear()
        if self.subject_list:
            for row in self.subject_list:
                self.ui.subject_cb.addItem(row[1])
                self.current_subject = self.subject_list[0][0]
        # Загрузка разделов и инициализация Treeview с деревом разделов
        if self.current_subject:
            section_table = Section(cur)
            self.section_list = section_table.select_detail(self.current_subject)
            section_tree = Tree()
            section_tree.import_data(self.section_list, 0, 2, 3)
            self.ui.section_tv.model = QStandardItemModel()
            self.ui.section_tv.setModel(section_tree.model)
            self.ui.section_tv.header().resizeSection(0, 250)
            self.ui.section_tv.expandAll()
        else:
            self.error_dialog.showMessage('Не выбран предмет')

    def open_action(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "Файлы БД (*.mtdb);;All Files (*)", options=options)
        if file_name:
            self.statusBar().showMessage('Открыт файл ' + file_name)
            self.db_file = file_name
            self.load_data()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec())
