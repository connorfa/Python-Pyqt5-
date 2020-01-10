from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import  QtPrintSupport
from PyQt5.QtPrintSupport import  QPrinter
import sys
from change_password1 import Ui_Dialog
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import  QRegExpValidator
from PyQt5.QtSql import QSqlQuery,QSqlDatabase,QSqlTableModel,QSqlRelation,QSqlRelationalDelegate, QSqlRelationalTableModel
#from PyQt5.QtWidgets import QMainWindow,QDialog, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from change_password1 import Ui_Dialog
import q11
import copy
import pymssql   #连接数据库
from teacher1 import teacher1
import xlsxwriter
class teacher2(QtWidgets.QMainWindow,teacher1):
    def __init__(self, ipname, parent=None):
        super(teacher2,self).__init__(parent )
        self.setupUi(self)
        '''将登陆的ip账号对应的名字放在idname(label）中'''
        self.ipname1 = ipname    #从登陆窗口得到的ip账号，即学生的学号
        print("this is ipname1",self.ipname1)
        conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
        curs = conn.cursor()
        if not curs:
            raise Exception('数据库连接失败！')
        cu = conn.cursor()
        cu.execute("select tno,tname from teacher")#似乎因为tno属性为10位字符，而数据为8位，所以出现无法传值的问题
        row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
        print("this is row",row)
        print("this is str=",str(row[0][0]).split(' ')[0])
        print("type row[0][0]=",type(row[0][0]))
        for i in range(len(row)):
            if self.ipname1==str(row[i][0]).split(' ')[0]:
                self.idname.setText(row[i][1])
                break

        '''信号槽的连接'''
        self.zhuxiao.clicked.connect(self.close)
        self.xiu_mima.clicked.connect(self.changepassword)
        self.comboBox.currentIndexChanged.connect(self.combo1)  # 点击comboBox时发射信号
        self.bt1.clicked.connect(self.search)
        self.comboBox_3.currentIndexChanged.connect(self.combo3)
        self.comboBox_4.currentIndexChanged.connect(self.combo4)
        #self.btn2.clicked.connect(self.handle_print)#打印
        self.btn2.clicked.connect(self.on_pushButton_print_clicked)
    def changepassword(self):
        self.childpass = childpassword()  # 实例化子窗口
        self.childpass.show()
    def combo1(self, i):
        if self.comboBox.currentText() == "课表查询":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(0, "")
            self.comboBox_2.addItem("课程号")
            self.comboBox_2.addItem("课程名")
            #self.comboBox_2.currentIndexChanged.connect(self.combo2)
        if self.comboBox.currentText() == "学生查询":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(0, "")
            self.comboBox_2.addItem("学号")
            self.comboBox_2.addItem("姓名")
            self.comboBox_2.addItem("所属院系")
        if self.comboBox.currentText() == "院系":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(0, "")
            self.comboBox_2.addItem("院系号")
            self.comboBox_2.addItem("院系名")
    def search(self):
        self.test1 = self.id.text()
        if len(self.test1) == 0:
            QMessageBox.warning(self, "警告", "请填写信息")
        else:
            id1=self.id.text()
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            '''创建一个cursor了。通过这个对象来对数据库发送一个请求操作'''
            curs = conn.cursor()
            '''发送SQL命令到数据库服务器了'''
            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn.cursor()
            s_value=0#用于判断linedit的值是否有在数据库中
            if self.comboBox_2.currentText() == "课程号" or self.comboBox_2.currentText() == "课程名":
                cu.execute("select * from course ")
                row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):

                    if str(row[i][0]).split(' ')[0]==self.test1 or str(row[i][1]).split(' ')[0]==self.test1:
                        #print(row[i])
                        row1=row[i]

                        c1 = QHBoxLayout()
                        self.table1.setRowCount(1)
                        self.table1.setColumnCount(4)
                        c1.addWidget(self.table1)
                        print(self.comboBox.currentText())
                        self.table1.setHorizontalHeaderLabels(['课程号','课程名','先修课程','学分'])
                        #for i in range(len(row)):
                        for j in range(4):
                              '''new=QTableWidgetItem(str(row[i][j]))
                              self.table1.setItem(i,j,new)
                              new = QTableWidgetItem(str(row[i][j]))
                              self.table1.setItem(i, j, new)
                              new = QTableWidgetItem(str(row[i][j]))
                              self.table1.setItem(i, j, new)
                              new = QTableWidgetItem(str(row[i][j]))
                              self.table1.setItem(i, j, new)'''
                              new = QTableWidgetItem(str(row1[j]))
                              self.table1.setItem(0, j, new)
                              new = QTableWidgetItem(str(row1[j]))
                              self.table1.setItem(0, j, new)
                              new = QTableWidgetItem(str(row1[j]))
                              self.table1.setItem(0, j, new)
                              new = QTableWidgetItem(str(row1[j]))
                              self.table1.setItem(0, j, new)
                        self.setLayout(c1)
                        conn.close()
                        self.id.clear()
                        s_value=1
                if s_value==0:
                    QMessageBox.warning(self, "警告", "不存在该查询信息")


            elif self.comboBox_2.currentText() == "学号" or self.comboBox_2.currentText() == "姓名":

                cu.execute("select * from student ")
                row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    # print(str(row[i][1]).split(' ')[0])
                    if str(row[i][0]).split(' ')[0] == self.test1 or str(row[i][1]).split(' ')[0] == self.test1:
                        # print(row[i])
                        row1 = row[i]
                        print("thie is ", row1)
                        c1 = QHBoxLayout()
                        self.table1.setRowCount(1)
                        self.table1.setColumnCount(5)
                        c1.addWidget(self.table1)
                        print(self.comboBox.currentText())
                        self.table1.setHorizontalHeaderLabels(['学号', '姓名', '性别', '年龄','所属院系'])
                        # for i in range(len(row)):
                        for j in range(5):
                            new = QTableWidgetItem(str(row1[j]))
                            self.table1.setItem(0, j, new)
                            new = QTableWidgetItem(str(row1[j]))
                            self.table1.setItem(0, j, new)
                            new = QTableWidgetItem(str(row1[j]))
                            self.table1.setItem(0, j, new)
                            new = QTableWidgetItem(str(row1[j]))
                            self.table1.setItem(0, j, new)
                            new = QTableWidgetItem(str(row1[j]))
                            self.table1.setItem(0, j, new)

                        self.setLayout(c1)
                        conn.close()
                        self.id.clear()
                        s_value = 1
                if s_value==0:
                    QMessageBox.warning(self, "警告", "不存在该查询信息")
            elif self.comboBox_2.currentText() == "所属院系":
                cu.execute("select sno,sname,ssex,sage,sdept from student where sdept='%s' "%(self.test1))
                row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                c1 = QHBoxLayout()
                self.table1.setRowCount(len(row))
                self.table1.setColumnCount(5)
                c1.addWidget(self.table1)
                self.table1.setHorizontalHeaderLabels(['学号', '姓名', '性别', '年龄', '所属院系'])
                for i in range(len(row)):
                    for j in range(5):
                        new = QTableWidgetItem(str(row[i][j]))
                        self.table1.setItem(i, j, new)
                        new = QTableWidgetItem(str(row[i][j]))
                        self.table1.setItem(i, j, new)
                        new = QTableWidgetItem(str(row[i][j]))
                        self.table1.setItem(i, j, new)
                        new = QTableWidgetItem(str(row[i][j]))
                        self.table1.setItem(i, j, new)
                        new = QTableWidgetItem(str(row[i][j]))
                        self.table1.setItem(i, j, new)
                cu1 = conn.cursor()
                cu1.execute(" select count(sno) from student where sdept='%s' "%(self.test1))
                row1 = cu1.fetchone()
                self.sum2.setText(str(row1[0]))



            elif self.comboBox_2.currentText() == "院系号" or self.comboBox_2.currentText() == "院系名":
                #QMessageBox.warning(self, "警告", "密码长度低于6位")
                cu.execute("select * from department ")
                row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    # print(str(row[i][1]).split(' ')[0])
                    if str(row[i][0]).split(' ')[0] == self.test1 or str(row[i][1]).split(' ')[0] == self.test1:
                        # print(row[i])
                        row1 = row[i]

                        c1 = QHBoxLayout()
                        self.table1.setRowCount(1)
                        self.table1.setColumnCount(3)
                        c1.addWidget(self.table1)
                        print(self.comboBox.currentText())
                        self.table1.setHorizontalHeaderLabels(['院系号', '院系名', '管理员'])
                        # for i in range(len(row)):
                        for j in range(3):
                            new = QTableWidgetItem(str(row1[j]))
                            self.table1.setItem(0, j, new)
                            new = QTableWidgetItem(str(row1[j]))
                            self.table1.setItem(0, j, new)
                            new = QTableWidgetItem(str(row1[j]))
                            self.table1.setItem(0, j, new)
                        self.setLayout(c1)
                        conn.close()
                        self.id.clear()
                        s_value = 1
                if s_value == 0:
                    QMessageBox.warning(self, "警告", "不存在该查询信息")
    def combo3(self, i):
        if self.comboBox_3.currentText() == "学生":
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn.cursor()

            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn.cursor()
            cu.execute("select * from student")
            row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
            print(row)
            c1 = QHBoxLayout()
            self.table2.setRowCount(len(row))
            self.table2.setColumnCount(5)
            c1.addWidget(self.table2)
            self.table2.setHorizontalHeaderLabels(['学号', '姓名', '性别', '年龄','所属院系'])
            for i in range(len(row)):
                for j in range(5):
                    new=QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i,j,new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
            #统计学生人数
            cu1=conn.cursor()
            cu1.execute(" select count(sno) from student")
            row1=cu1.fetchone()
            self.sum.setText(str(row1[0]))
            #self.setLayout(c1)
            #conn.close()
        if self.comboBox_3.currentText() == "教师":
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn.cursor()

            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn.cursor()
            cu.execute("select * from teacher")
            row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
            print(row)
            c1 = QHBoxLayout()
            self.table2.setRowCount(len(row))
            self.table2.setColumnCount(9)
            c1.addWidget(self.table2)
            self.table2.setHorizontalHeaderLabels(['教工号', '教工名', '性别', '年龄','学历','职称','主讲课程1','主讲课程2','主讲课程3'])
            for i in range(len(row)):
                for j in range(9):
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
            self.setLayout(c1)
            conn.close()
        if self.comboBox_3.currentText() == "院系":
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn.cursor()

            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn.cursor()
            cu.execute("select * from department")
            row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
            print(row)
            c1 = QHBoxLayout()
            self.table2.setRowCount(len(row))
            self.table2.setColumnCount(3)
            c1.addWidget(self.table2)
            self.table2.setHorizontalHeaderLabels(['院系号', '院系名', '管理人'])
            for i in range(len(row)):
                for j in range(3):
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
            cu1 = conn.cursor()
            cu1.execute(" select count(dno) from department")
            row1 = cu1.fetchone()
            self.sum.setText(str(row1[0]))
            self.setLayout(c1)
            conn.close()
        if self.comboBox_3.currentText() == "课程":
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn.cursor()

            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn.cursor()
            cu.execute("select * from course")
            row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
            c1 = QHBoxLayout()
            self.table2.setRowCount(len(row))
            self.table2.setColumnCount(4)
            c1.addWidget(self.table2)
            self.table2.setHorizontalHeaderLabels(['课程号','课程名','先修课程','学分'])
            for i in range(len(row)):
                for j in range(4):
                    new=QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i,j,new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table2.setItem(i, j, new)
            cu1 = conn.cursor()
            cu1.execute(" select count(cno) from course")
            row1 = cu1.fetchone()
            self.sum.setText(str(row1[0]))
            self.setLayout(c1)
            conn.close()
    def combo4(self, i):

        if self.comboBox_4.currentText() == "已修课程":
            conn1 = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn1.cursor()

            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn1.cursor()
            cu.execute("select sct.sno,cno,tno,grate,student.sdept from sct,student where grate is not null and student.sno=sct.sno ")
            row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
            row = [list(item) for item in row if item[2] == self.ipname1] #将属于该学号的课程选出来

            c2 = QHBoxLayout()
            self.table3.setRowCount(len(row))
            self.table3.setColumnCount(5)
            c2.addWidget(self.table3)
            self.table3.setHorizontalHeaderLabels(['学号', '课程号', '教工号', '成绩','学院'])


            for i in range(len(row)):
                for j in range(5):
                    new=QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i,j,new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
            cu1 = conn1.cursor()
            cu1.execute(" select count(sno) from sct where  grate is not null and tno='%s'"%(self.ipname1))
            row1 = cu1.fetchone()
            self.sum1.setText(str(row1[0]))
            self.setLayout(c2)
            conn1.close
        if self.comboBox_4.currentText() == "已选课程":
            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn.cursor()

            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn.cursor()
            cu.execute("select * from sct where grate is null and tno='%s'" % (self.ipname1))
            row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
            print(row)
            c1 = QHBoxLayout()
            self.table3.setRowCount(len(row))
            self.table3.setColumnCount(4)
            c1.addWidget(self.table3)
            self.table3.setHorizontalHeaderLabels(['学号', '课程号', '教工号', '成绩'])
            for i in range(len(row)):
              #if row[i][4] == ' ':
                for j in range(4):
                    new=QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i,j,new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
            cu1 = conn.cursor()
            cu1.execute(" select count(sno) from sct where grate is null and tno='%s'" % (self.ipname1))
            row1 = cu1.fetchone()
            self.sum1.setText(str(row1[0]))


    def handle_print(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)

        dialog = QtPrintSupport.QPrintDialog(printer, self)

        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:

            self.handle_paint_request(printer)

    def handle_preview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handle_paint_request)
        dialog.exec_()

    def handle_paint_request(self, printer):

        painter = QtGui.QPainter(printer)

        painter.setViewport(self.chart_view.rect())
        painter.setWindow(self.chart_view.rect())
        self.chart_view.render(painter)
        painter.end()

    def on_pushButton_print_clicked(self):

        rows = self.table3.rowCount()
        columns = self.table3.columnCount()

        shuju = []
        for i in range(rows):
            data = []
            for j in range(columns):
                data.append(self.table3.item(i, j).text())
            shuju.append(data)

        workbook = xlsxwriter.Workbook('C:\\Users\\ASUS\\Desktop\\pp\\aaa.xlsx')  # 创建一个Excel文件

        worksheet = workbook.add_worksheet()  # 创建一个sheet
        row = 1
        col = 0
        biaotou=[]
        for i in range(columns):
            biaotou.append(self.table3.horizontalHeaderItem(i).text())
        for j in range(len(biaotou)):
            worksheet.write(0, j, str(biaotou[j]))

        if columns == 5:
            for item, cost, ee ,g,k in (shuju):
                worksheet.write(row, col, item)
                worksheet.write(row, col + 1, cost)
                worksheet.write(row, col + 2, ee)
                worksheet.write(row, col + 3, g)
                worksheet.write(row, col + 4, k)
                row += 1
        workbook.close()
        answer = QMessageBox.information(self, "消息", "成功导出到excel", QMessageBox.Ok)


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

    myshow=teacher2()

    myshow.show()#窗口全屏
    sys.exit(app.exec_())