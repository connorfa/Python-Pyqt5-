# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_function.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
import q11
import pymssql
from PyQt5.QtSql import QSqlQuery,QSqlDatabase,QSqlTableModel,QSqlRelation,QSqlRelationalDelegate, QSqlRelationalTableModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(120, 40, 481, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabe = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tabe.setObjectName("tabe")
        self.gridLayout.addWidget(self.tabe, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.bt1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.bt1.setObjectName("bt1")

        self.bt1.clicked.connect(self.view_data)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "添加学生"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "删除学生"))
        self.bt1.setText(_translate("MainWindow", "添加学生"))


    def view_data(self):
        '''db = QSqlDatabase.addDatabase("QODBC")  # select database type
        db.setHostName("localhost")  # set address
        db.setDatabaseName("Course_Management")
        db.setUserName("sa");  # set user name
        db.setPassword("ROOT");  # set user pwd
        # self._trytoConnect()  # check connection'''
        db = QSqlDatabase.addDatabase("QODBC")
        db.setDatabaseName("Driver={Sql Server};Server=localhost;Database=Course_Management;Uid=sa;Pwd=ROOT")
        db.open()
        # 实例化一个可编辑数据模型
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("zhanghao")  # 设置数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改
        #self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
        self.model.select()  # 查询所有数据

        # 设置表格头
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, '站点名称')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, '站点地址')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, '站点地址')
        self.tabe.setModel(self.model)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = Ui_MainWindow()
    myshow.show()  # 窗口全屏
    query = QSqlQuery()
    sys.exit(app.exec_())