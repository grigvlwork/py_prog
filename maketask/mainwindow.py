# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.subject_cb = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subject_cb.sizePolicy().hasHeightForWidth())
        self.subject_cb.setSizePolicy(sizePolicy)
        self.subject_cb.setEditable(False)
        self.subject_cb.setObjectName("subject_cb")
        self.horizontalLayout_3.addWidget(self.subject_cb)
        self.subject_add = QtWidgets.QPushButton(self.centralwidget)
        self.subject_add.setObjectName("subject_add")
        self.horizontalLayout_3.addWidget(self.subject_add)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.section_tv = QtWidgets.QTreeView(self.centralwidget)
        self.section_tv.setHeaderHidden(True)
        self.section_tv.setObjectName("section_tv")
        self.section_tv.header().setDefaultSectionSize(0)
        self.section_tv.header().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.section_tv)
        self.task_list_view = QtWidgets.QListView(self.centralwidget)
        self.task_list_view.setObjectName("task_list_view")
        self.horizontalLayout.addWidget(self.task_list_view)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.section_add = QtWidgets.QPushButton(self.centralwidget)
        self.section_add.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.section_add.setIcon(icon)
        self.section_add.setObjectName("section_add")
        self.horizontalLayout_2.addWidget(self.section_add)
        self.section_del = QtWidgets.QPushButton(self.centralwidget)
        self.section_del.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pictures/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.section_del.setIcon(icon1)
        self.section_del.setObjectName("section_del")
        self.horizontalLayout_2.addWidget(self.section_del)
        self.section_edit = QtWidgets.QPushButton(self.centralwidget)
        self.section_edit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pictures/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.section_edit.setIcon(icon2)
        self.section_edit.setObjectName("section_edit")
        self.horizontalLayout_2.addWidget(self.section_edit)
        self.task_add = QtWidgets.QPushButton(self.centralwidget)
        self.task_add.setText("")
        self.task_add.setIcon(icon)
        self.task_add.setObjectName("task_add")
        self.horizontalLayout_2.addWidget(self.task_add)
        self.task_del = QtWidgets.QPushButton(self.centralwidget)
        self.task_del.setText("")
        self.task_del.setIcon(icon1)
        self.task_del.setObjectName("task_del")
        self.horizontalLayout_2.addWidget(self.task_del)
        self.task_edit = QtWidgets.QPushButton(self.centralwidget)
        self.task_edit.setText("")
        self.task_edit.setIcon(icon2)
        self.task_edit.setObjectName("task_edit")
        self.horizontalLayout_2.addWidget(self.task_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.add_task_to_work = QtWidgets.QPushButton(self.centralwidget)
        self.add_task_to_work.setObjectName("add_task_to_work")
        self.horizontalLayout_5.addWidget(self.add_task_to_work)
        self.del_task_from_work = QtWidgets.QPushButton(self.centralwidget)
        self.del_task_from_work.setObjectName("del_task_from_work")
        self.horizontalLayout_5.addWidget(self.del_task_from_work)
        self.create_work = QtWidgets.QPushButton(self.centralwidget)
        self.create_work.setObjectName("create_work")
        self.horizontalLayout_5.addWidget(self.create_work)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.works_list = QtWidgets.QPushButton(self.centralwidget)
        self.works_list.setObjectName("works_list")
        self.horizontalLayout_6.addWidget(self.works_list)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.task_in_work_list = QtWidgets.QListView(self.centralwidget)
        self.task_in_work_list.setObjectName("task_in_work_list")
        self.verticalLayout.addWidget(self.task_in_work_list)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_act = QtWidgets.QAction(MainWindow)
        self.new_act.setObjectName("new_act")
        self.open_act = QtWidgets.QAction(MainWindow)
        self.open_act.setObjectName("open_act")
        self.save_act = QtWidgets.QAction(MainWindow)
        self.save_act.setEnabled(False)
        self.save_act.setObjectName("save_act")
        self.saveas_act = QtWidgets.QAction(MainWindow)
        self.saveas_act.setEnabled(False)
        self.saveas_act.setObjectName("saveas_act")
        self.exit_act = QtWidgets.QAction(MainWindow)
        self.exit_act.setObjectName("exit_act")
        self.insert_act = QtWidgets.QAction(MainWindow)
        self.insert_act.setEnabled(False)
        self.insert_act.setObjectName("insert_act")
        self.del_act = QtWidgets.QAction(MainWindow)
        self.del_act.setEnabled(False)
        self.del_act.setObjectName("del_act")
        self.edit_act = QtWidgets.QAction(MainWindow)
        self.edit_act.setEnabled(False)
        self.edit_act.setObjectName("edit_act")
        self.help_act = QtWidgets.QAction(MainWindow)
        self.help_act.setObjectName("help_act")
        self.about_act = QtWidgets.QAction(MainWindow)
        self.about_act.setObjectName("about_act")
        self.menu.addAction(self.new_act)
        self.menu.addAction(self.open_act)
        self.menu.addAction(self.save_act)
        self.menu.addAction(self.saveas_act)
        self.menu.addSeparator()
        self.menu.addAction(self.exit_act)
        self.menu_2.addAction(self.insert_act)
        self.menu_2.addAction(self.del_act)
        self.menu_2.addAction(self.edit_act)
        self.menu_3.addAction(self.help_act)
        self.menu_3.addAction(self.about_act)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конструктор заданий"))
        self.label.setText(_translate("MainWindow", "Предмет"))
        self.subject_add.setText(_translate("MainWindow", "Добавить предмет"))
        self.section_add.setToolTip(_translate("MainWindow", "Добавить раздел"))
        self.section_del.setToolTip(_translate("MainWindow", "Удалить раздел"))
        self.section_edit.setToolTip(_translate("MainWindow", "Редактировать раздел"))
        self.task_add.setToolTip(_translate("MainWindow", "Добавить задачу"))
        self.task_del.setToolTip(_translate("MainWindow", "Удалить задачу"))
        self.task_edit.setToolTip(_translate("MainWindow", "Редактировать задачу"))
        self.add_task_to_work.setText(_translate("MainWindow", "Добавить задачи в работу"))
        self.del_task_from_work.setText(_translate("MainWindow", "Удалить задачи из работы"))
        self.create_work.setText(_translate("MainWindow", "Сформировать работу"))
        self.works_list.setText(_translate("MainWindow", "Перейти к списку работ"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Редактировать"))
        self.menu_3.setTitle(_translate("MainWindow", "Помощь"))
        self.new_act.setText(_translate("MainWindow", "Новый"))
        self.open_act.setText(_translate("MainWindow", "Открыть"))
        self.save_act.setText(_translate("MainWindow", "Сохранить"))
        self.saveas_act.setText(_translate("MainWindow", "Сохранить как"))
        self.exit_act.setText(_translate("MainWindow", "Выход"))
        self.insert_act.setText(_translate("MainWindow", "Добавить"))
        self.del_act.setText(_translate("MainWindow", "Удалить"))
        self.edit_act.setText(_translate("MainWindow", "Редактировать"))
        self.help_act.setText(_translate("MainWindow", "Справка"))
        self.about_act.setText(_translate("MainWindow", "О программе"))
