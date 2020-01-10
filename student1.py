from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import  QRegExpValidator
from PyQt5.QtSql import QSqlQuery,QSqlDatabase,QSqlTableModel,QSqlRelation,QSqlRelationalDelegate, QSqlRelationalTableModel
from PyQt5.QtWidgets import QMainWindow,QDialog, QApplication, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QKeyEvent, QKeySequence, QRegExpValidator
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from change_password1 import Ui_Dialog
import q11
import copy
import pymssql   #连接数据库
#from student import student
from student2 import student
class student1(QtWidgets.QMainWindow,student):
    #ipname1=None
    def __init__(self,ipname,parent=None):
        super(student1,self).__init__(parent )
        self.setupUi(self)
        '''将登陆的ip账号对应的名字放在idname(label）中'''
        self.ipname1=ipname     #从登陆窗口得到的ip账号，即学生的学号
        #print("this is ipname1",ipname1)
        conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
        curs = conn.cursor()
        if not curs:
            raise Exception('数据库连接失败！')
        cu = conn.cursor()
        cu.execute("select sno,sname from student")
        row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
        for i in range(len(row)):
            if self.ipname1==row[i][0]:
                self.idname.setText(row[i][1])
                break
        #self.idname.setText(self.ipname1)
        #self.idname.setText(self.comboBox.currentText()) #将点击comboBox的列的值在idname显示出来
        '''信号槽的连接'''
        self.zhuxiao.clicked.connect(self.close)
        self.xiu_mima.clicked.connect(self.changepassword)
        self.bt2.clicked.connect(self.xuanke)
        self.comboBox.currentIndexChanged.connect(self.combo1)#点击comboBox时发射信号
        self.comboBox_3.currentIndexChanged.connect(self.combo3)
        self.comboBox_4.currentIndexChanged.connect(self.combo4)

        self.bt1.clicked.connect(self.search)
    def changepassword(self):
        self.childpass = childpassword()  # 实例化子窗口
        self.childpass.show()
    def combo1(self, i):
        if self.comboBox.currentText() == "课表查询":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("课程号")
            self.comboBox_2.addItem("课程名")
            #self.comboBox_2.currentIndexChanged.connect(self.combo2)
        if self.comboBox.currentText() == "教师":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(0, "")
            self.comboBox_2.addItem("教工号")
            self.comboBox_2.addItem("教工名")
        if self.comboBox.currentText() == "院系":
            self.comboBox_2.clear()
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(0, "")
            self.comboBox_2.addItem("院系号")
            self.comboBox_2.addItem("院系名")
    '''def combo2(self,i):
        self.test1 = self.id.text()
        print("b")
        a = 0
        if self.comboBox_2.currentText() == "课程号" or self.comboBox_2.currentText() == "课程名":
            print("yfgfs")
            conn1 = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs1 = conn1.cursor()
            if not curs1:
                raise Exception('数据库连接失败！')
            cun = conn1.cursor()
            cun.execute("select cno,cname from course ")
            print("kkkk")
            row1 = cun.fetchall()
        self.bt1.clicked.connect(self.search)'''
    def combo4(self, i):
        if self.comboBox_4.currentText() == "学生":
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
            #self.setLayout(c1)
            #conn.close()
        if self.comboBox_4.currentText() == "教师":
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

        if self.comboBox_4.currentText() == "院系":
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
            self.setLayout(c1)
            conn.close()
        if self.comboBox_4.currentText() == "课程":
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
            self.setLayout(c1)
            conn.close()

    def combo3(self, i):

        if self.comboBox_3.currentText() == "已修课程":
            self.table3.clearContents()#清处表格数据
            conn1 = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn1.cursor()

            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn1.cursor()
            cu.execute("select * from sct where grate is not null")
            row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
            row = [list(item) for item in row if item[0] == self.ipname1] #将属于该学号的


            c2 = QHBoxLayout()
            self.table3.setRowCount(len(row))
            self.table3.setColumnCount(4)
            c2.addWidget(self.table3)
            self.table3.setHorizontalHeaderLabels(['学号', '课程号', '教工号', '成绩'])


            for i in range(len(row)):
                for j in range(4):
                    new=QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i,j,new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
            #self.setLayout(c2)
            #conn1.close
        if self.comboBox_3.currentText() == "已选课程":

            conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
            curs = conn.cursor()

            if not curs:
                raise Exception('数据库连接失败！')
            cu = conn.cursor()
            cu.execute("select * from sct where grate is null")
            row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
            print(row)
            c1 = QHBoxLayout()
            self.table3.setRowCount(len(row))
            self.table3.setColumnCount(4)
            c1.addWidget(self.table3)
            self.table3.setHorizontalHeaderLabels(['学号', '课程号', '教工号', '取消选课'])
            for i in range(len(row)):
              #if row[i][4] == ' ':
                for j in range(4):
                    new=QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i,j,new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
                    new = QTableWidgetItem(str(row[i][j]))
                    self.table3.setItem(i, j, new)
                    btn5 = MyButton(self)
                    btn5.setText("取消选课")
                    self.table3.setCellWidget(i, 3, btn5)

                    btn5.clicked.connect(lambda: self.quxiaobtn(row, btn5))
                    #print("this is test21")

            #self.setLayout(c1)
            conn.close()
    def quxiaobtn(self,row,btn5):
        row1 = self.table3.currentItem().row()

        conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
        curs = conn.cursor()
        if not curs:
            raise Exception('数据库连接失败！')
        cu1 = conn.cursor()
        sno1=str(row[row1][0]).split(' ')[0]

        cno1=str(row[row1][1]).split(' ')[0]

        tno1=str(row[row1][2]).split(' ')[0]
        try:
            cu1.execute("delete from sct where sno='%s' and cno='%s' and tno='%s' and grate is null" % (sno1,cno1,tno1))
            conn.commit()
            answer = QMessageBox.information(self, "消息", "成功取消选课，请刷新！", QMessageBox.Ok)
        except Exception as e:
            answer = QMessageBox.information(self, "消息", "修改数据库失败", QMessageBox.Ok)
        conn.close()



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


            elif self.comboBox_2.currentText() == "教工号" or self.comboBox_2.currentText() == "教工名":
                #QMessageBox.warning(self, "警告", "密码长度低于6位")
                cu.execute("select * from teacher ")
                row = cu.fetchall()  # fetchall方法返回所有匹配的元组，给出一个大元组（每个元素还是一个元组）
                for i in range(len(row)):
                    # print(str(row[i][1]).split(' ')[0])
                    if str(row[i][0]).split(' ')[0] == self.test1 or str(row[i][1]).split(' ')[0] == self.test1:
                        # print(row[i])
                        row1 = row[i]
                        print("thie is ", row1)
                        c1 = QHBoxLayout()
                        self.table1.setRowCount(1)
                        self.table1.setColumnCount(9)
                        c1.addWidget(self.table1)
                        print(self.comboBox.currentText())
                        self.table1.setHorizontalHeaderLabels(['教工号', '教工名', '性别', '年龄','学历','职称','主讲课程1','主讲课程2','主讲课程3'])
                        # for i in range(len(row)):
                        for j in range(9):
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
    def xuanke(self):
        conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
        '''创建一个cursor了。通过这个对象来对数据库发送一个请求操作'''
        curs = conn.cursor()
        '''发送SQL命令到数据库服务器了'''
        if not curs:
            raise Exception('数据库连接失败！')
        cu1 = conn.cursor()
        cu1.execute("select cno,cname,cpno,ccredit from course  ")
        row1 = cu1.fetchall()

        cu2=conn.cursor()
        cu2.execute("select tname,cno1,cno2,cno3 from teacher")
        row2=cu2.fetchall()

        self.bt3 = QtWidgets.QPushButton()
        s1=[]
        s1=[list(item) for item in row1]
        print(s1)
        s2=[]
        s2=[list(item ) for item in row2]
        print(s2)
        s=[]
        k=0
        for j in range(len(s2)):
            for i in range(len(s1)):
                if str(s1[i][1]).split(' ')[0]==str(s2[j][1]).split(' ')[0] or str(s1[i][1]).split(' ')[0]== str(s2[j][2]).split(' ')[0] or str(s1[i][1]).split(' ')[0] == str(s2[j][3]).split(' ')[0]:
                    s3 = copy.deepcopy(s1)
                    s.append(s3[i])
                    ss=s2[j][0]

                    s[k].append(ss)
                    k=k+1

 #从sct表中获取到row3,主要用于在选课时不出现已修过的课程
        cu3 = conn.cursor()
        cu3.execute("select sno ,cno from sct")
        row3=cu3.fetchall()
        row3=[list(item) for item in row3 if item[0]==self.ipname1]

#处理选课表中该学号已选过的课程
        for i in s[:]:
            for k in row3:
                if k[1]==i[0]:
                    index=s.index(i)
                    #s.pop(index)
                    del s[index]

        c1 = QHBoxLayout()
        self.table4.setRowCount(len(s))
        self.table4.setColumnCount(6)
        c1.addWidget(self.table4)
        self.table4.setHorizontalHeaderLabels(['课程号', '课程名', '先行课程', '学分', '教师', '选课'])
        for i in range(len(s)):
                    for j in range(5):

                      new = QTableWidgetItem(str(s[i][j]))
                      self.table4.setItem(i, j, new)
                      new = QTableWidgetItem(str(s[i][j]))
                      self.table4.setItem(i, j, new)
                      new = QTableWidgetItem(str(s[i][j]))
                      self.table4.setItem(i, j, new)
                      new = QTableWidgetItem(str(s[i][j]))
                      self.table4.setItem(i, j, new)
                      new = QTableWidgetItem(str(s[i][j]))
                      self.table4.setItem(i, j, new)
                      btn4=MyButton(self)
                      btn4.setText("选课")

                      self.table4.setCellWidget(i,5,btn4)
                      btn4.clicked.connect(lambda :self.xuankebtn(s,btn4))
        self.setLayout(c1)
        conn.close()
#选课步骤：要先点一下表格中那一行的单元格，再点按键
    def xuankebtn(self,s,btn):

        #answer = QMessageBox.information(self, "消息", "选课成功，请重新刷新", QMessageBox.Ok)
        row1=self.table4.currentItem().row()#获取到所点击表格的单元格的所在行数
        conn = pymssql.connect(host='localhost', user='sa', password='ROOT', database='Course_Management')
        curs = conn.cursor()
        if not curs:
            raise Exception('数据库连接失败！')
        cu1 = conn.cursor()
        cu1.execute("select tno from teacher where tname='%s'"%(s[row1][4]))
        row2=cu1.fetchone()
        tname1=str(row2[0]).split(' ')[0]
        #查看该学号所选课程是否超过两门
        cu2=conn.cursor()
        cu2.execute("select count(cno) from sct where sno='%s' and grate is null"%(self.ipname1))
        row3=cu2.fetchone()
        if row3[0]<2:
        #grade=0
          try:
            cu=conn.cursor()
            cu.execute("insert into sct(sno,cno,tno) values('%s','%s','%s')" % (self.ipname1, s[row1][0], tname1))
            conn.commit()
            answer = QMessageBox.information(self, "消息", "选课成功，请重新刷新", QMessageBox.Ok)
          except Exception as e:
            print(e)
            ans = QMessageBox.information(self, "消息", "修改数据库失败,请联系管理员！", QMessageBox.Ok)
          conn.close()
        else:
            answer = QMessageBox.information(self, "消息", "限选两门", QMessageBox.Ok)

        '''self.btn=dynamic_cast<QPushButton>(self.sender())
        print("this btn 's s",s)
        if (self.btn==0):
            return
        x=self.btn.frameGeometry().x()
        print("x=",x)
        y=self.btn.frameGeometry().y()
        index=table4.indexAt(QPoint(x,y))
        row=index.row()
        colum=index.column()'''


class MyButton(QtWidgets.QToolButton):
      '''自定义按钮类'''
      def __init__(self,parent=None):
        super(MyButton,self).__init__(parent)
      def mousepress(self,event):
          if event.button()==QtCore.Qt.LeftButton:
              # 发射点击信号
              self.clicked.emit(True)
              # 传递至父窗口响应鼠标按下事件
              self.parent().mousepress(event)



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

    myshow=student1()

    myshow.show()#窗口全屏
    sys.exit(app.exec_())