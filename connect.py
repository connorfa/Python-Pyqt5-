from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from change_password1 import Ui_Dialog
from insert import *
#from denglu_jiemian import login_MainWindow
from zhuce import zhuce_MainWindow
from denglu_jiemian1 import Ui_MainWindow
#from main_function1 import main_function
#from main_function2 import main_function#管理员界面类
from main_function3 import main_function
from student1 import student1
from teacher2 import teacher2
import sys
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import  QRegExpValidator
from PyQt5.QtSql import QSqlQuery,QSqlDatabase,QSqlTableModel,QSqlRelation,QSqlRelationalDelegate, QSqlRelationalTableModel
from PyQt5.QtWidgets import QMainWindow,QDialog, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5.QtGui import *
import hashlib
#class mywindow(QtWidgets.QMainWindow,login_MainWindow):
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(mywindow,self).__init__(parent )
        self.setupUi(self)

        #self.child=childwindow() #实例化子窗口
        self.child=childwindow()#实例化
        self.bt2.clicked.connect(self.click_child)#跳转到注册窗口


        self.function=childmain_function()#实例化管理员登陆界面
        #self.s_function=student1("0")#实例化学生登陆界面
        #self.s_function=student1()
        self.bt1.clicked.connect(self.connectdb)#跳转到登陆界面
        #self.bt1.clicked.connect(self.close)#跳转的同时关闭父窗口
        self.bt3.clicked.connect(self.click_childpasswd)#跳转到修改密码界面

        # 设置验证
        reg=QRegExp("[a-zA-Z0-9]+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.id.setValidator(pValidator)
        pValidator.setRegExp(reg)
        self.password.setValidator(pValidator)
        self.password.setContextMenuPolicy(Qt.NoContextMenu)
        self.password.setPlaceholderText( "字母开头")
        self.password.setEchoMode(QLineEdit.Password)
        reg1 = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(reg1,self.password)
        self.password.setValidator(validator)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pixmap = QtGui.QPixmap("C:\\Users\\ASUS\\Desktop\\数据库201624131127吴佩婷\\吴佩婷选课系统代码\\图片\\t28.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def connectdb(self):#与bt1（登陆键）连接
        self.test = self.password.text()
        self.test1=self.id.text()

        md5 = hashlib.md5()
        md5.update(self.test.encode('utf-8'))  # 通过update将要加密的byte放进md5
        self.test = md5.hexdigest()
        print("passwd=",self.test)
        if len(self.test) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        elif len(self.test) < 6:
            QMessageBox.warning(self, "警告", "密码长度不可低于6位")
        else:
            id1 = self.id.text()
            passwd = self.password.text()
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            '''创建一个cursor了。通过这个对象来对数据库发送一个请求操作'''
            curs = conn.cursor()
            '''发送SQL命令到数据库服务器了'''
            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn.cursor()
            cu.execute("select id,password,symbol from zhanghao")
            row = cu.fetchall()#fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
            print(row)
            a = 0
            #b = 0  #作为账号是否等于学生表/老师表，切换界面
            '''for id in  range(len(row)):
                print(row[id][2])
                if str(row[id][2]).split(' ')[0]=='a':
                    b=1

                # if id[2].split('')
                #     b=1'''
            for i in range(len(row)):
                #print(str(row[i][2]).split(' ')[0])

                if row[i][0]==self.test1 and row[i][1]==self.test and str(row[i][2]).split(' ')[0]=='a':##管理员登陆的地方
                    reply=QMessageBox.information(self,"消息","登陆成功", QMessageBox.Ok)
                    a = 1
                    self.function.showMaximized()                   #点击按键后跳转登陆界面的show()
                    self.id.clear()
                    self.password.clear()

                #这里修改了，若发生错误，删除即可，
                elif row[i][0] == self.test1 and row[i][1] == self.test and str(row[i][2]).split(' ')[0] == 's':
                    reply = QMessageBox.information(self, "消息", "登陆成功", QMessageBox.Ok)
                    a = 1
                    ipname=self.id.text()
                    #self.s_function2=student1(ipname)
                    self.s_function = student1(ipname)
                    #self.s_function = student1()
                    self.s_function.showMaximized()  # 点击按键后跳转登陆界面的show()
                    self.id.clear()
                    self.password.clear()
                elif row[i][0] == self.test1 and row[i][1] == self.test and str(row[i][2]).split(' ')[0] == 't':
                    reply = QMessageBox.information(self, "消息", "登陆成功", QMessageBox.Ok)
                    a = 1
                    ipname = self.id.text()
                    #self.s_function2=student1(ipname)
                    self.t=teacher2(ipname)

                    self.t.showMaximized()  # 点击按键后跳转登陆界面的show()
                    self.id.clear()
                    self.password.clear()


                elif str(row[i][0]).split(' ')[0]==self.test1 and str(row[i][1]).split(' ')[0]!=self.test:
                    reply = QMessageBox.information(self, "消息", "密码错误", QMessageBox.Ok)
                    a = 1
            if a == 0:
                reply = QMessageBox.information(self, "消息", "账号不存在", QMessageBox.Ok)
            #conn.close()
            #self.exec_()

    def click_child(self):
        # self.child=childwindow() #实例化子窗口
        self.child.showMaximized()
    def click_childpasswd(self):
        self.childpass=childpassword() #实例化子窗口
        self.childpass.show()
#class childwindow(QtWidgets.QDialog,Ui_Dialog):#继承子窗口的类
class childmain_function(QtWidgets.QMainWindow,main_function):#管理员界面的类
    def __init__(self):
        super(childmain_function, self).__init__()
        self.setupUi(self)

        db = QSqlDatabase.addDatabase("QODBC")
        db.setDatabaseName("Driver={Sql Server};Server=localhost;Database=Course_Management;Uid=sa;Pwd=ROOT")
        db.open()
        '''self.model = QtSql.QSqlTableModel()
        self.model.setTable("zhanghao")  # 设置数据模型的数据表
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改
        self.table_view.setModel(self.model)'''

        '''信号槽'''
        #账号
        self.bt1.clicked.connect(self.view_data)
        self.bt2.clicked.connect(self.add_row_data)
        self.bt3.clicked.connect(self.del_row_data)
        self.bt4.clicked.connect(self.change_data)
        self.bt5.clicked.connect(self.return_change)
        self.bt6.clicked.connect(self.search_data)
        #学生
        self.s_bt1.clicked.connect(self.s_view_data)
        self.s_bt2.clicked.connect(self.s_add_data)
        self.s_bt3.clicked.connect(self.s_del_data)
        self.s_bt4.clicked.connect(self.s_change_data)
        self.s_bt5.clicked.connect(self.s_return_change)
        self.s_bt6.clicked.connect(self.s_search_data)
        #教师
        self.t_bt1.clicked.connect(self.t_view_data)
        self.t_bt2.clicked.connect(self.t_add_data)
        self.t_bt3.clicked.connect(self.t_del_data)
        self.t_bt4.clicked.connect(self.t_change_data)
        self.t_bt5.clicked.connect(self.t_return_change)
        self.t_bt6.clicked.connect(self.t_search_data)
        #院系
        self.d_bt1.clicked.connect(self.d_view_data)
        self.d_bt2.clicked.connect(self.d_add_data)
        self.d_bt3.clicked.connect(self.d_del_data)
        self.d_bt4.clicked.connect(self.d_change_data)
        self.d_bt5.clicked.connect(self.d_return_change)
        self.d_bt6.clicked.connect(self.d_search_data)
        #课程
        self.c_bt1.clicked.connect(self.c_view_data)
        self.c_bt2.clicked.connect(self.c_add_data)
        self.c_bt3.clicked.connect(self.c_del_data)
        self.c_bt4.clicked.connect(self.c_change_data)
        self.c_bt5.clicked.connect(self.c_return_change)
        self.c_bt6.clicked.connect(self.c_search_data)
        #选课
        self.x_bt1.clicked.connect(self.x_view_data)
        self.x_bt2.clicked.connect(self.x_add_data)
        self.x_bt3.clicked.connect(self.x_del_data)
        #self.x_bt6.clicked.connect(self.x_search_tno)
        #self.x_bt5.clicked.connect(self.x_search_cno)
        self.x_bt4.clicked.connect(self.x_search_data)


    def view_data(self):

            # 实例化一个可编辑数据模型
            self.model = QtSql.QSqlTableModel()
            self.model.setTable("zhanghao")  # 设置数据模型的数据表
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改
            # self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model.select()  # 查询所有数据

            # 设置表格头
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, '账号')
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, '密码')
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, '身份凭证')
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, '标志')
            self.table_view.setModel(self.model)
            self.table_view.setColumnWidth(0, 150)
            self.table_view.setColumnWidth(1, 150)
            self.table_view.setColumnWidth(2, 150)#对第二列的单元格设置宽度
            self.table_view.setColumnWidth(3, 150)

    def add_row_data(self):
            # 如果存在实例化的数据模型对象
            self.model.insertRows(self.model.rowCount(), 1)
            self.model.submitAll()
        # 删除一行数据
    def del_row_data(self):
            self.table_view.setModel(self.model)
            self.model.removeRow(self.table_view.currentIndex().row())
            answer = QMessageBox.question(self, "警告", "确定删除当前行", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if answer == QMessageBox.No:
                self.model.revertAll()
            else:
                self.model.submitAll()
    def change_data(self):
            self.model.database().transaction()
            if (self.model.submitAll()):
                self.model.database().commit()
            else:
                self.model.database().rollback()
                QMessageBox.Warning(self, "警告", "数据库错误")
    def return_change(self):
            self.model.revertAll()
    def search_data(self):
            id1 = self.id.text()
            self.model.setFilter("id='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
            print("you are crazy")
            self.model.select()
            # self.table_view.setModel(self.model)
##对学生表的增删查改
    def s_view_data(self):

            # 实例化一个可编辑数据模型
            self.model2 = QtSql.QSqlTableModel()
            self.model2.setTable("student")  # 设置数据模型的数据表
            self.model2.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改
            # self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model2.select()  # 查询所有数据

            # 设置表格头
            self.model2.setHeaderData(0, QtCore.Qt.Horizontal, '学号')
            self.model2.setHeaderData(1, QtCore.Qt.Horizontal, '姓名')
            self.model2.setHeaderData(2, QtCore.Qt.Horizontal, '性别')
            self.model2.setHeaderData(3, QtCore.Qt.Horizontal, '年龄')
            self.model2.setHeaderData(4, QtCore.Qt.Horizontal, '所属院系')
            self.table_view2.setModel(self.model2)
            self.table_view2.setColumnWidth(0, 170)
            self.table_view2.setColumnWidth(1, 170)
            self.table_view2.setColumnWidth(2, 170)  # 对第二列的单元格设置宽度
            self.table_view2.setColumnWidth(3, 170)
            self.table_view2.setColumnWidth(4, 170)

    def s_add_data(self):
            # 如果存在实例化的数据模型对象

            self.model2.insertRows(self.model2.rowCount(), 1)
            self.model2.submitAll()

        # 删除一行数据
    def s_del_data(self):
            self.table_view2.setModel(self.model2)
            self.model2.removeRow(self.table_view2.currentIndex().row())
            answer = QMessageBox.question(self, "警告", "确定删除当前行", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if answer == QMessageBox.No:
                self.model2.revertAll()
            else:
                self.model2.submitAll()

    def s_change_data(self):

            self.model2.database().transaction()
            if (self.model2.submitAll()):
                self.model2.database().commit()
            else:
                self.model2.database().rollback()
                QMessageBox.Warning(self, "警告", "数据库错误")

    def s_return_change(self):
            self.model2.revertAll()

    def s_search_data(self):
            '''id1 = self.s_id.text()
            self.model2.setFilter("sno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
            self.model2.select()
            # self.table_view.setModel(self.model)'''
            id1 = self.s_id.text()
            self.sum1.clear()
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn.cursor()
            if not curs:
                raise Exception('数据库连接失败！')

            s_value = 0  # 用于判断linedit的值是否有在数据库中

            if self.comboBox.currentText() == "学号":
                curs.execute("select * from student ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][0]).split(' ')[0] ==self.s_id.text() :
                        s_value=1
                self.model2.setFilter("sno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model2.select()
                cu1 = conn.cursor()
                cu1.execute(" select count(sno) from student where  sno='%s'" % (id1))
                row1 = cu1.fetchone()
                self.sum1.setText(str(row1[0]))
            elif self.comboBox.currentText() == "姓名":
                curs.execute("select * from student ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][1]).split(' ')[0] ==self.s_id.text() :
                        s_value=1
                self.model2.setFilter("sname='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model2.select()
                cu1 = conn.cursor()
                cu1.execute(" select count(sname) from student where  sname='%s'" % (id1))
                row1 = cu1.fetchone()
                self.sum1.setText(str(row1[0]))
            elif self.comboBox.currentText() == "所属学院":
                curs.execute("select * from student ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][4]).split(' ')[0] ==self.s_id.text() :
                        s_value=1
                print("111")
                self.model2.setFilter("sdept='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model2.select()
                print("Kk")
                cu1 = conn.cursor()
                cu1.execute(" select count(sno) from student where  sdept='%s'" % (id1))
                print("Jj")
                row1 = cu1.fetchone()
                self.sum1.setText(str(row1[0]))
            elif self.comboBox.currentText() == "性别":
                curs.execute("select * from student ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][2]).split(' ')[0] ==self.s_id.text() :
                        s_value=1
                print("111")
                self.model2.setFilter("ssex='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model2.select()
                print("Kk")
                cu1 = conn.cursor()
                cu1.execute(" select count(sno) from student where  ssex='%s'" % (id1))
                print("Jj")
                row1 = cu1.fetchone()
                self.sum1.setText(str(row1[0]))
            if s_value==1:
                QMessageBox.warning(self, "提示", "查询成功")
            else:
                QMessageBox.warning(self, "警告", "不存在该查询信息")




##对教师表的增删查改
    def t_view_data(self):

            # 实例化一个可编辑数据模型
            self.model3 = QtSql.QSqlTableModel()
            self.model3.setTable("teacher")  # 设置数据模型的数据表
            self.model3.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改
            # self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model3.select()  # 查询所有数据

            # 设置表格头
            self.model3.setHeaderData(0, QtCore.Qt.Horizontal, '教工号')
            self.model3.setHeaderData(1, QtCore.Qt.Horizontal, '姓名')
            self.model3.setHeaderData(2, QtCore.Qt.Horizontal, '性别')
            self.model3.setHeaderData(3, QtCore.Qt.Horizontal, '年龄')
            self.model3.setHeaderData(4, QtCore.Qt.Horizontal, '学历')
            self.model3.setHeaderData(5, QtCore.Qt.Horizontal, '职称')
            self.model3.setHeaderData(6, QtCore.Qt.Horizontal, '主讲课程1')
            self.model3.setHeaderData(7, QtCore.Qt.Horizontal, '主讲课程2')
            self.model3.setHeaderData(8, QtCore.Qt.Horizontal, '主讲课程3')

            self.table_view3.setModel(self.model3)

    def t_add_data(self):
            # 如果存在实例化的数据模型对象

            self.model3.insertRows(self.model3.rowCount(), 1)
            self.model3.submitAll()

        # 删除一行数据
    def t_del_data(self):
            self.table_view3.setModel(self.model3)
            self.model3.removeRow(self.table_view3.currentIndex().row())
            answer = QMessageBox.question(self, "警告", "确定删除当前行", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if answer == QMessageBox.No:
                self.model3.revertAll()
            else:
                self.model3.submitAll()

    def t_change_data(self):

            self.model3.database().transaction()
            if (self.model3.submitAll()):
                self.model3.database().commit()
            else:
                self.model3.database().rollback()
                QMessageBox.Warning(self, "警告", "数据库错误")

    def t_return_change(self):
            self.model3.revertAll()

    def t_search_data(self):
            '''id1 = self.t_id.text()

            self.model3.setFilter("tno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句

            self.model3.select()
            # self.table_view.setModel(self.model)'''
            id1 = self.t_id.text()
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn.cursor()
            if not curs:
                raise Exception('数据库连接失败！')

            value = 0  # 用于判断linedit的值是否有在数据库中

            if self.comboBox_2.currentText() == "教工号":
                curs.execute("select * from teacher ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][0]).split(' ')[0] == self.t_id.text():
                        value = 1
                self.model3.setFilter("tno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句

                self.model3.select()
                cu1 = conn.cursor()
                cu1.execute(" select count(tno) from teacher where  tno='%s'" % (id1))
                row1 = cu1.fetchone()
                self.sum2.setText(str(row1[0]))
            elif self.comboBox_2.currentText() == "姓名":
                curs.execute("select * from teacher ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][1]).split(' ')[0] == self.t_id.text():
                        value = 1
                self.model3.setFilter("tname='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句

                self.model3.select()
                cu1 = conn.cursor()
                cu1.execute(" select count(tname) from teacher where tname='%s'" % (id1))
                row1 = cu1.fetchone()
                self.sum2.setText(str(row1[0]))
            elif self.comboBox_2.currentText() == "所教课程":
                curs.execute("select * from teacher ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][6]).split(' ')[0] == self.t_id.text() or str(row[i][7]).split(' ')[0] == self.t_id.text()\
                            or str(row[i][8]).split(' ')[0] == self.t_id.text():
                        value = 1
                print("111")
                self.model3.setFilter("cno1='%s' or cno2='%s' or cno3='%s' " % (id1,id1,id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句

                self.model3.select()
                print("Kk")
                cu1 = conn.cursor()
                cu1.execute(" select count(tno) from teacher where  cno1='%s' or cno2='%s' or cno3='%s' " % (id1,id1,id1))
                print("Jj")
                row1 = cu1.fetchone()
                self.sum2.setText(str(row1[0]))
            elif self.comboBox_2.currentText() == "性别":
                curs.execute("select * from teacher ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][2]).split(' ')[0] == self.t_id.text():
                        value = 1
                print("111")
                self.model3.setFilter("tsex='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句

                self.model3.select()
                print("Kk")
                cu1 = conn.cursor()
                cu1.execute(" select count(tno) from teacher where  tsex='%s'" % (id1))
                print("Jj")
                row1 = cu1.fetchone()
                self.sum2.setText(str(row1[0]))
            if value == 1:
                #QMessageBox.warning(self, "提示", "查询成功")
                print("ok")
            else:
                QMessageBox.warning(self, "警告", "不存在该查询信息")


##对院系进行增删查改
    def d_view_data(self):

            # 实例化一个可编辑数据模型
            self.model4 = QtSql.QSqlTableModel()
            self.model4.setTable("department")  # 设置数据模型的数据表
            self.model4.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改
            # self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model4.select()  # 查询所有数据

            # 设置表格头
            self.model4.setHeaderData(0, QtCore.Qt.Horizontal, '院系号')
            self.model4.setHeaderData(1, QtCore.Qt.Horizontal, '院系名')
            self.model4.setHeaderData(2, QtCore.Qt.Horizontal, '系主任')


            self.table_view4.setModel(self.model4)

    def d_add_data(self):
            # 如果存在实例化的数据模型对象

            self.model4.insertRows(self.model4.rowCount(), 1)#1表示增加一行表格用于添加
            self.model4.submitAll()

        # 删除一行数据
    def d_del_data(self):
            self.table_view4.setModel(self.model4)
            self.model4.removeRow(self.table_view4.currentIndex().row())
            answer = QMessageBox.question(self, "警告", "确定删除当前行", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if answer == QMessageBox.No:
                self.model4.revertAll()
            else:
                self.model4.submitAll()

    def d_change_data(self):

            self.model4.database().transaction()
            if (self.model4.submitAll()):
                self.model4.database().commit()
            else:
                self.model4.database().rollback()
                QMessageBox.Warning(self, "警告", "数据库错误")

    def d_return_change(self):
            self.model4.revertAll()

    def d_search_data(self):
            id1 = self.d_id.text()

            self.model4.setFilter("dno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
            print("you are crazy")
            self.model4.select()
            # self.table_view.setModel(self.model)
##对课程表的增删查改
    def c_view_data(self):
            '''self.MyTable = QtWidgets.QTableWidget()
            self.MyTable.setHorizontalHeaderLabels(['课程好', '课程名', '先前课程', '学分', '选课'])'''

            # 实例化一个可编辑数据模型
            self.model5 = QtSql.QSqlTableModel()
            self.model5.setTable("course")  # 设置数据模型的数据表
            self.model5.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改
            # self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model5.select()  # 查询所有数据

            # 设置表格头
            self.model5.setHeaderData(0, QtCore.Qt.Horizontal, '课程号')
            self.model5.setHeaderData(1, QtCore.Qt.Horizontal, '课程名')
            self.model5.setHeaderData(2, QtCore.Qt.Horizontal, '先前课程')
            self.model5.setHeaderData(3, QtCore.Qt.Horizontal, '学分')

            self.table_view5.setModel(self.model5)


    def c_add_data(self):
            # 如果存在实例化的数据模型对象

            self.model5.insertRows(self.model5.rowCount(), 1)
            self.model5.submitAll()

        # 删除一行数据
    def c_del_data(self):
            self.table_view5.setModel(self.model5)
            self.model5.removeRow(self.table_view5.currentIndex().row())
            answer = QMessageBox.question(self, "警告", "确定删除当前行", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if answer == QMessageBox.No:
                self.model5.revertAll()
            else:
                self.model5.submitAll()

    def c_change_data(self):
            self.model5.database().transaction()
            if (self.model5.submitAll()):
                self.model5.database().commit()
            else:
                self.model5.database().rollback()
                QMessageBox.Warning(self, "警告", "数据库错误")

    def c_return_change(self):
            self.model5.revertAll()

    def c_search_data(self):
            id1 = self.c_id.text()

            self.model5.setFilter("cno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
            print("you are crazy")
            self.model5.select()
            # self.table_view.setModel(self.model)


##对课程表的增删查改
    def x_view_data(self):

            # 实例化一个可编辑数据模型
            self.model6 = QtSql.QSqlTableModel()
            self.model6.setTable("sct")  # 设置数据模型的数据表
            self.model6.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)  # 允许字段更改
            # self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)  # 允许字段更改
            self.model6.select()  # 查询所有数据

            # 设置表格头
            self.model6.setHeaderData(0, QtCore.Qt.Horizontal, '学号')
            self.model6.setHeaderData(1, QtCore.Qt.Horizontal, '课程号')
            self.model6.setHeaderData(2, QtCore.Qt.Horizontal, '教工号')
            self.model6.setHeaderData(3, QtCore.Qt.Horizontal, '成绩')

            self.table_view6.setModel(self.model6)

    def x_add_data(self):
            # 如果存在实例化的数据模型对象

            self.model6.insertRows(self.model6.rowCount(), 1)
            self.model6.submitAll()

        # 删除一行数据
    def x_del_data(self):
            self.table_view6.setModel(self.model6)
            self.model6.removeRow(self.table_view6.currentIndex().row())
            answer = QMessageBox.question(self, "警告", "确定删除当前行", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if answer == QMessageBox.No:
                self.model6.revertAll()
            else:
                self.model6.submitAll()

    def x_change_data(self):
            self.model6.database().transaction()
            if (self.model6.submitAll()):
                self.model6.database().commit()
            else:
                self.model6.database().rollback()
                QMessageBox.Warning(self, "警告", "数据库错误")

    def x_return_change(self):
            self.model6.revertAll()

    def x_search_data(self):
            '''id1 = self.x_id1.text()
            self.model6.setFilter("sno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
            self.model6.select()
            # self.table_view.setModel(self.model)'''
            id1 = self.x_id1.text()
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn.cursor()
            if not curs:
                raise Exception('数据库连接失败！')

            value = 0  # 用于判断linedit的值是否有在数据库中
            if self.comboBox_3.currentText() == "学号":
                curs.execute("select * from sct ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][0]).split(' ')[0] ==self.x_id1.text() :
                        s_value=1
                self.model6.setFilter("sno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model6.select()
                cu1 = conn.cursor()
                cu1.execute(" select count(sno) from sct where  sno='%s'" % (id1))
                row1 = cu1.fetchone()
                self.sum3.setText(str(row1[0]))
            elif  self.comboBox_3.currentText() == "教工号":
                curs.execute("select * from sct ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][2]).split(' ')[0] == self.x_id1.text():
                        value = 1
                self.model6.setFilter("tno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model6.select()
                cu1 = conn.cursor()
                cu1.execute(" select count(tno) from sct where  tno='%s'" % (id1))
                row1 = cu1.fetchone()
                self.sum3.setText(str(row1[0]))
            elif self.comboBox_3.currentText() == "课程号":
                curs.execute("select * from sct ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][1]).split(' ')[0] == self.x_id1.text():
                        value = 1
                self.model6.setFilter("cno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model6.select()
                cu1 = conn.cursor()
                cu1.execute(" select count(cno) from sct where cno='%s'" % (id1))
                row1 = cu1.fetchone()
                self.sum3.setText(str(row1[0]))
            elif self.comboBox_3.currentText() == "课程号":
                curs.execute("select * from sct ")
                row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    if str(row[i][6]).split(' ')[0] == self.x_id1.text() :
                        value = 1
                print("111")
                self.model6.setFilter("sno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model6.select()
                print("Kk")
                cu1 = conn.cursor()
                cu1.execute(
                    " select count(sno) from sct where  cno='%s' " % (id1))
                print("Jj")
                row1 = cu1.fetchone()
                self.sum3.setText(str(row1[0]))
            elif self.comboBox_3.currentText() == "成绩合格":
                curs.execute("select count(sno) from sct where grate>='%d' ",(60))
                #row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                row = curs.fetchone()

                if row[0]!=0:
                    value = 1
                self.model6.setFilter("grate>='%d' " % (60))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model6.select()

                cu1 = conn.cursor()
                cu1.execute(" select count(sno) from sct where  grate>='%d'" % (60))
                row1 = cu1.fetchone()
                self.sum3.setText(str(row1[0]))
            elif self.comboBox_3.currentText() == "成绩不合格":
                curs.execute("select count(sno) from sct where grate<'%d' ",(60))
                #row = curs.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                row = curs.fetchone()
                print("row",row[0])

                if row[0]!=0:
                    value = 1
                self.model6.setFilter("grate<'%d' " % (60))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
                self.model6.select()
                cu1 = conn.cursor()
                cu1.execute(" select count(sno) from sct where  grate<'%d'" % (60))
                row1 = cu1.fetchone()
                self.sum3.setText(str(row1[0]))
            if value == 0:
                QMessageBox.warning(self, "警告", "不存在该查询信息")
    def x_search_cno(self):
            id1 = self.x_id2.text()
            self.model6.setFilter("cno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
            self.model6.select()
    def x_search_tno(self):
            id1 = self.x_id3.text()
            self.model6.setFilter("tno='%s'" % (id1))  # 筛选，按照字符串对数据库进行筛选，相当于SQL中的WHERE语句
            self.model6.select()
class childwindow(QtWidgets.QMainWindow,zhuce_MainWindow):#注册账号的类
    def __init__(self):
        super(childwindow,self).__init__()
        self.setupUi(self)
        #设置验证
        reg = QRegExp("[a-zA-Z0-9]+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.id.setValidator(pValidator)

        self.password.setContextMenuPolicy(Qt.NoContextMenu)
        self.password.setPlaceholderText("字母开头")
        self.password.setEchoMode(QLineEdit.Password)
        reg1 = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(reg1, self.password)
        self.password.setValidator(validator)

        self.btn.clicked.connect(self.connect1)

    def connect1(self):



        self.text1 = self.id.text()
        self.text2=self.password.text()
#对其进行加密
        md5 = hashlib.md5()
        md5.update(self.text2.encode('utf-8'))  # 通过update将要加密的byte放进md5
        self.text2 = md5.hexdigest()
        print(md5.hexdigest())
        if  len(self.text1) == 0 or len(self.text2) == 0:
            QMessageBox.warning(self, "警告", "请正确填写信息")

        elif len(self.text2) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
        else:
            if self.stu.isChecked() or self.tch.isChecked() or self.admin.isChecked():
                symbol = ''
                if self.stu.isChecked():
                    symbol='s'
                elif self.tch.isChecked():
                    symbol='t'
                else:
                    symbol='a'
                id1=self.id.text()
                passw=self.password.text()
                birth=self.yan.text()
                conn1 = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
                '''创建一个cursor了。通过这个对象来对数据库发送一个请求操作'''
                curs1 = conn1.cursor()
                '''发送SQL命令到数据库服务器了'''
                if not curs1:
                    raise Exception('数据库连接失败！')
                cun = conn1.cursor()
                cun.execute("select id,password from zhanghao")#连接账号表
                row1 = cun.fetchall()#fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                s_cun = conn1.cursor()
                s_cun.execute("select sno from student")
                s_row=s_cun.fetchall()
                t_cun=conn1.cursor()
                t_cun.execute("select tno from teacher")
                t_row=t_cun.fetchall()
                a = 0
                b = 0
                for i in range (len(s_row)):
                    if s_row[i][0]==self.text1:
                        b=1
                for i in range(len(t_row)):
                    if t_row[i][0]==self.text1:
                        b=1
                if b==1:
                  for i in range(len(row1)):
                    if row1[i][0] == self.text1:
                        answer = QMessageBox.information(self, "消息", "该账号已存在", QMessageBox.Ok)
                        a = 1
                  if a == 0:
                    print("2=",md5.hexdigest())
                    answer = QMessageBox.information(self, "消息", "申请成功", QMessageBox.Ok)
                    cun.execute("insert into zhanghao values('% s','% s','% s','% s')" % (id1, md5.hexdigest(), birth, symbol))
                    conn1.commit()
                    if answer == QMessageBox.Ok:
                        self.close()
                    # conn1.close()
                    # self.exec_()
                else:
                    answer = QMessageBox.information(self, "消息", "该账号不正确", QMessageBox.Ok)
            else:#对应的if是if self.stu.isChecked() or self.tch.isChecked() or self.admin.isChecked():
                QMessageBox.warning(self, "警告", "请选择身份属性")
                '''for i in range(len(row1)):
                    if row1[i][0]==self.text1:
                        answer= QMessageBox.information(self, "消息", "该账号已存在", QMessageBox.Ok)
                        a=1
                if a==0:
                    answer = QMessageBox.information(self, "消息", "申请成功", QMessageBox.Ok)
                    cun.execute("insert into zhanghao values('% s','% s','% s','% s')" % (id1,passw,birth,symbol))
                    conn1.commit()
                    if answer == QMessageBox.Ok:
                        self.close()
                    #conn1.close()
                    #self.exec_()
            else:##对应if self.stu.isChecked() or self.tch.isChecked() or self.admin.isChecked():
                QMessageBox.warning(self, "警告", "请选择身份属性")'''
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pixmap = QtGui.QPixmap("C:\\Users\\ASUS\\Desktop\\pp\\图片\\t28.jpg")
        painter.drawPixmap(self.rect(), pixmap)

class childpassword(QtWidgets.QDialog,Ui_Dialog):#密码的类
    def __init__(self):
        super(childpassword, self).__init__()
        self.setupUi(self)
        # 设置验证
        reg = QRegExp("[a-zA-Z0-9]+$")
        pValidator = QRegExpValidator(self)
        pValidator.setRegExp(reg)
        self.id.setValidator(pValidator)

        self.password.setContextMenuPolicy(Qt.NoContextMenu)
        self.password.setPlaceholderText("字母开头")
        self.password.setEchoMode(QLineEdit.Password)
        reg1 = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(reg1, self.password)
        self.password.setValidator(validator)

        self.btn1.clicked.connect(self.connectpasswd)
        #self.btn1.clicked.connect(self.close)
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pixmap = QtGui.QPixmap("C:\\Users\\ASUS\\Desktop\\pp\\图片\\t24.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def connectpasswd(self):#与bt3（登陆键）连接
        self.test1 = self.id.text()
        self.test2 = self.password.text()
        self.test3 = self.yan.text()
        if len(self.test1) == 0 or len(self.test2) == 0 or len(self.test3)==0:
            QMessageBox.warning(self, "警告", "请正确填写信息")
        elif len(self.test2) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
        else:
            conn1 = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            '''创建一个cursor了。通过这个对象来对数据库发送一个请求操作'''
            curs1 = conn1.cursor()
            '''发送SQL命令到数据库服务器了'''
            if not curs1:
                raise Exception('数据库连接失败！')
            cun = conn1.cursor()
            cun.execute("select id,birth,password from zhanghao")
            row1 = cun.fetchall()
            a = 0
            b = 0
            id1 = self.id.text()
            passw = self.password.text()
            birth1 = self.yan.text()
            for i in range(len(row1)):
              if row1[i][0] == self.test1 and row1[i][1]==self.test3 and row1[i][2]!=self.test2:
                  answer = QMessageBox.information(self, "消息", "成功修改密码", QMessageBox.Ok)
                  if answer==QMessageBox.Ok:
                      self.close()
                  a = 1
                  cun.execute("update zhanghao set password='%s' where id='%s' "%(passw ,id1))
                  conn1.commit()
            for i in range(len(row1)):
                if row1[i][0] == self.test1 and row1[i][1] != self.test3:
                    answer = QMessageBox.information(self, "消息", "身份凭证错误", QMessageBox.Ok)
                    a = 1
                    break
                elif row1[i][0]==self.test1 and row1[i][1] == self.test3 and row1[i][2]==self.test2:
                    answer=QMessageBox.information(self, "消息", "密码已经存在", QMessageBox.Ok)
                    a = 1
            if a == 0:
                answer = QMessageBox.information(self, "消息", "该账号不存在", QMessageBox.Ok)
                self.exec_()



if __name__=='__main__':

    app=QApplication(sys.argv)
    myshow=mywindow()
    myshow.showMaximized()#窗口全屏
    sys.exit(app.exec_())

