# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_wordbooks.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(357, 268)
        Dialog.setStyleSheet("background-color: rgb(255, 220, 244);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 220, 244);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 5)
        self.button_choose = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.button_choose.setFont(font)
        self.button_choose.setStyleSheet("border-color: rgb(0, 0, 101);\n"
"background-color: rgb(255, 149, 206);")
        self.button_choose.setAutoRepeatDelay(240)
        self.button_choose.setAutoRepeatInterval(70)
        self.button_choose.setObjectName("button_choose")
        self.gridLayout.addWidget(self.button_choose, 1, 0, 1, 1)
        self.button_create = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.button_create.setFont(font)
        self.button_create.setStyleSheet("border-color: rgb(0, 0, 101);\n"
"background-color: rgb(255, 149, 206);")
        self.button_create.setAutoRepeatDelay(240)
        self.button_create.setAutoRepeatInterval(70)
        self.button_create.setObjectName("button_create")
        self.gridLayout.addWidget(self.button_create, 1, 1, 1, 1)
        self.button_change = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.button_change.setFont(font)
        self.button_change.setStyleSheet("border-color: rgb(0, 0, 101);\n"
"background-color: rgb(255, 149, 206);")
        self.button_change.setAutoRepeatDelay(240)
        self.button_change.setAutoRepeatInterval(70)
        self.button_change.setObjectName("button_change")
        self.gridLayout.addWidget(self.button_change, 1, 2, 1, 1)
        self.button_delete = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet("border-color: rgb(0, 0, 101);\n"
"background-color: rgb(255, 149, 206);")
        self.button_delete.setAutoRepeatDelay(240)
        self.button_delete.setAutoRepeatInterval(70)
        self.button_delete.setObjectName("button_delete")
        self.gridLayout.addWidget(self.button_delete, 1, 3, 1, 1)
        self.button_quit = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.button_quit.setFont(font)
        self.button_quit.setStyleSheet("border-color: rgb(0, 0, 101);\n"
"background-color: rgb(255, 149, 206);")
        self.button_quit.setAutoRepeatDelay(240)
        self.button_quit.setAutoRepeatInterval(70)
        self.button_quit.setObjectName("button_quit")
        self.gridLayout.addWidget(self.button_quit, 1, 4, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "管理单词本"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "词汇数"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "创建日期"))
        self.button_choose.setText(_translate("Dialog", "选中(C)"))
        self.button_choose.setShortcut(_translate("Dialog", "Alt+C"))
        self.button_create.setText(_translate("Dialog", "新建(N)"))
        self.button_create.setShortcut(_translate("Dialog", "Alt+N"))
        self.button_change.setText(_translate("Dialog", "修改(M)"))
        self.button_change.setShortcut(_translate("Dialog", "Alt+M"))
        self.button_delete.setText(_translate("Dialog", "删除(D)"))
        self.button_delete.setShortcut(_translate("Dialog", "Alt+D"))
        self.button_quit.setText(_translate("Dialog", "取消(Q)"))
        self.button_quit.setShortcut(_translate("Dialog", "Alt+Q"))
