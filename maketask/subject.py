# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subject.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_subject_edit_form(object):
    def setupUi(self, subject_edit_form):
        subject_edit_form.setObjectName("subject_edit_form")
        subject_edit_form.resize(400, 77)
        self.verticalLayout = QtWidgets.QVBoxLayout(subject_edit_form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(subject_edit_form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_edit = QtWidgets.QLineEdit(subject_edit_form)
        self.name_edit.setObjectName("name_edit")
        self.horizontalLayout.addWidget(self.name_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(subject_edit_form)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(subject_edit_form)
        self.buttonBox.accepted.connect(subject_edit_form.accept)
        self.buttonBox.rejected.connect(subject_edit_form.reject)
        QtCore.QMetaObject.connectSlotsByName(subject_edit_form)

    def retranslateUi(self, subject_edit_form):
        _translate = QtCore.QCoreApplication.translate
        subject_edit_form.setWindowTitle(_translate("subject_edit_form", "Редактирование предмета"))
        self.label.setText(_translate("subject_edit_form", "Название предмета"))
