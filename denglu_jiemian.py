# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denglu_jiemian.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from insert import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtSql
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import  QRegExpValidator
from PyQt5.QtSql import *
import q11

class login_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_2.setGeometry(QtCore.QRect(290, 250, 75, 23))
        #self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(200, 180, 341, 211))
        self.groupBox.setStyleSheet("QGroupBox{border:none;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 20, 24, 16))
        self.label.setObjectName("label")
        self.id = QtWidgets.QLineEdit(self.groupBox)
        self.id.setGeometry(QtCore.QRect(130, 20, 141, 20))
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 54, 12))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(130, 90, 141, 20))
        self.password.setObjectName("password")
        self.bt1 = QtWidgets.QPushButton(self.groupBox)
        self.bt1.setGeometry(QtCore.QRect(20, 150, 75, 23))
        self.bt1.setObjectName("bt1")
        self.bt2 = QtWidgets.QPushButton(self.groupBox)
        self.bt2.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.bt2.setObjectName("bt2")
        self.bt3 = QtWidgets.QPushButton(self.groupBox)
        self.bt3.setGeometry(QtCore.QRect(250, 150, 75, 23))
        self.bt3.setObjectName("bt3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生选课系统"))
        self.label.setText(_translate("MainWindow", "账号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.bt1.setText(_translate("MainWindow", "注册"))
        self.bt2.setText(_translate("MainWindow", "登陆"))
        self.bt3.setText(_translate("MainWindow", "忘记密码"))
        '''self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.showFullScreen()
        self.frame.setGeometry(QtCore.QRect(130, 100, 800,600))#原先参数为0，0，800，600
        self.frame.setStyleSheet("background-image: url(:/image/图片/t8.jpeg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #self.png=QtGui.QPixmap(self)
        #self.png.load("C:\\Users\\ASUS\\Desktop\\pp\\p3.jpg")
        #self.palette1=QtGui.QPalette(self)
        #self.palette1.setBrush(self.backgroundRole(),QtGui.QBrush(png))
        #self.widget
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 160, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 220, 51, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 300, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 300, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(190, 170, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("账号")#在Line中显示提示要输入的要求
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 220, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("密码")#在Line中显示提示要输入的要求
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.label_change)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.showFullScreen()'''


        ''' 
        # 设置验证
        reg = QRegExp("PB[0~9]{8}")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.lineEdit.setValidator(pValidator)

        pValidator.setRegExp(reg)
        self.lineEdit_2.setValidator(pValidator)

        id = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if (id == "1" or password == "1"):
                self.pushButton.clicked.connect(self.label_change)#与label_change连接修改label
        else:
                self.pushButton.clicked.connect(self.check_login)'''



    def label_change(self):#定义修改label的值
        self.label.setText("joying")
    def signInCheck(self):
        studentId = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if (studentId == "" or password == ""):
            print(QMessageBox.warning(self, "警告", "学号和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes))
            return
        # 打开数据库连接
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/LibraryManagement.db')
        db.open()
        query = QSqlQuery()
        sql = "SELECT * FROM user WHERE StudentId='%s'" % (studentId)
        query.exec_(sql)
        db.close()

        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        if (not query.next()):
            print(QMessageBox.information(self, "提示", "该账号不存在!", QMessageBox.Yes, QMessageBox.Yes))
        else:
            if (studentId == query.value(0) and hl.hexdigest() == query.value(2)):
                # 如果是管理员
                if (query.value(3)==1):
                    self.is_admin_signal.emit()
                else:
                    self.is_student_signal.emit(studentId)
            else:
                print(QMessageBox.information(self, "提示", "密码错误!", QMessageBox.Yes, QMessageBox.Yes))
        return

    '''def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.pushButton_2.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "账号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "注册"))
        self.pushButton_3.setText(_translate("MainWindow", "登陆"))
        self.pushButton_4.setText(_translate("MainWindow", "退出"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))'''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''    bu3=ui.pushButton_3
    bu3.clicked.connect(Ui_MainWindow.Main.show)'''


    #insert
''' ui.pushButton_3.clicked.connect(ui.click_pushb3, ui.)


    def click_pushb3(self):
        a = QtWidgets.QApplication(sys.argv)
        Main = insert.QtWidgets.QMainWindow()
        # ui = Ui_MainWindow()
        uii = insert.Ui_MainWindow()

        # ui.setupUi(MainWindow)
        uii.setupUi(Main)
        # MainWindow.show()
        Main.show()
        sys.exit(a.exec_())'''
