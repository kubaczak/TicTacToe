# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 400)
        self.btn1 = QtWidgets.QPushButton(Dialog)
        self.btn1.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.btn1.setText("")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(Dialog)
        self.btn2.setGeometry(QtCore.QRect(100, 0, 100, 100))
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(Dialog)
        self.btn3.setGeometry(QtCore.QRect(200, 0, 100, 100))
        self.btn3.setText("")
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(Dialog)
        self.btn4.setGeometry(QtCore.QRect(0, 100, 100, 100))
        self.btn4.setText("")
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(Dialog)
        self.btn5.setGeometry(QtCore.QRect(100, 100, 100, 100))
        self.btn5.setText("")
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(Dialog)
        self.btn6.setGeometry(QtCore.QRect(200, 100, 100, 100))
        self.btn6.setText("")
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(Dialog)
        self.btn7.setGeometry(QtCore.QRect(0, 200, 100, 100))
        self.btn7.setText("")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(Dialog)
        self.btn8.setGeometry(QtCore.QRect(100, 200, 100, 100))
        self.btn8.setText("")
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(Dialog)
        self.btn9.setGeometry(QtCore.QRect(200, 200, 100, 100))
        self.btn9.setText("")
        self.btn9.setObjectName("btn9")
        self.mainBtn = QtWidgets.QPushButton(Dialog)
        self.mainBtn.setGeometry(QtCore.QRect(190, 340, 75, 23))
        self.mainBtn.setObjectName("mainBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 330, 151, 41))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mainBtn.setText(_translate("Dialog", "Połącz"))
