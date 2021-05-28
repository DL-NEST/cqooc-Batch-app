# -*- coding: utf-8 -*-
import requests
import json
# import subprocess #进程管道
import time
import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from selenium import webdriver
from PyQt5 import QtCore, QtGui, QtWidgets
import configparser
import base64

#懒得读写文件，所以就摆在这了

list_num = [75657, 75658, 75660, 75661, 75662, 75663, 75664,
            75665, 75666, 75667, 75668, 75669, 75670, 75671, 75672, 75673, 75674, 75675, 75676, 75677, 75678, 75679,
            75680, 75681, 75682, 75683, 75684, 75685, 75686, 75687]

list_a = [{'q49374': '2', 'q49377': '1', 'q49378': '0', 'q49372': ['0', '1', '2'], 'q49371': '1', 'q49379': '1', 'q49380': '1'},{'q49471': '3', 'q49502': '0', 'q49525': '1', 'q49527': '0', 'q49529': '1', 'q49530': '0', 'q49539': '3', 'q49536': '1', 'q49531': '2', 'q49533': '1', 'q49534': '1', 'q49537': '1'},{'q50034': '1', 'q50041': '2', 'q50032': '1', 'q50033': '1', 'q50038': '1', 'q50039': '2', 'q50040': '1'},{'q51322': '1', 'q51323': '3', 'q51324': '0', 'q51325': '1', 'q51326': '2'},{'q51327': '0', 'q51328': '2', 'q51329': '2', 'q51330': '3', 'q51331': '0'},
{'q51332': '2', 'q51333': '2', 'q51334': '3', 'q51335': '0', 'q51336': '3'},{'q50617': '3', 'q50623': '3', 'q50624': '1', 'q50664': '1', 'q50666': '1', 'q50670': '3', 'q50673': ['0', '1', '2', '3', '4'], 'q50686': ['0', '1', '3']},{'q51162': '3', 'q51175': '0', 'q51176': '0', 'q50687': '1', 'q51161': '2'},{'q51280': '0', 'q51281': '3', 'q51282': '1', 'q51283': '1', 'q51284': '1', 'q51285': '3', 'q51204': '1'},{'q51286': '2', 'q51287': '1', 'q51288': '0', 'q51289': '2', 'q51290': '3'},{'q51317': '2', 'q51318': '1', 'q51319': '2', 'q51320': '1', 'q51321': '2'},{'q51338': '3', 'q51339': '0', 'q51340': '1', 'q51341': '1', 'q51342': '3', 'q51337': ['0', '2']},{'q51355': '3', 'q51356': '2', 'q51357': '2', 'q51358': '0', 'q51359': '1', 'q51360': '3', 'q51361': ['1', '2', '3'], 'q51362': ['0', '1', '2'], 'q51363': ['1', '3'], 'q51364': '1', 'q51365': '1'},{'q51349': '1', 'q51350': '2', 'q51351': '0', 'q51352': ['0', '1', '2', '3'], 'q51353': '1', 'q51354': '2'},
{'q51343': '3', 'q51344': '1', 'q51345': ['0', '1', '3'], 'q51346': '2', 'q51347': '2', 'q51348': '1'},{'q51368': '1', 'q51369': '3', 'q51370': '1', 'q51371': '1'},{'q51372': '1', 'q51373': ['0', '1', '2'], 'q51374': ['0', '1', '3'], 'q51375': ['0', '1']},{'q51380': '0', 'q51382': '1', 'q51383': '1', 'q51384': '3', 'q51385': '3', 'q51386': '3', 'q51388': '2', 'q51389': ['0', '2'], 'q51391': '2', 'q51392': '1', 'q51393': '2', 'q51394': '1'},{'q51396': '1', 'q51397': '0', 'q51398': '3', 'q51399': '1', 'q51400': ['1', '3'], 'q51401': '2', 'q51402': '2', 'q51403': '2'},
{"q49541":"0","q49548":"0","q49549":"3","q49550":"0","q49557":"1","q49558":"0","q49546":["0","1"],"q49547":["0","1","2"],"q49542":"1","q49543":"1","q49544":"1","q49559":"1"},{"q49961":"0","q49964":"0","q49960":"2","q49962":"1","q49963":"2","q49965":"2","q49966":"1"},{"q50043":"1","q50044":"2","q50050":"0","q50045":["1"],"q50042":"1","q50046":"2","q50047":"1","q50048":"2","q50049":"1"},{"q50070":"1","q50071":"2","q50072":"1","q50073":"0","q50074":"2","q50075":"2","q50076":"0","q50077":"2","q50078":["2","3"],"q50079":["1","2"]}, {"q50081":"0","q50082":"3","q50083":"2","q50084":"2","q50080":"1"}, {"q50086":"3","q50087":"2","q50088":"2","q50089":"0"},{"q50125":"1","q50128":"0","q50131":"1","q50167":"0","q50318":"3","q50122":"1","q50129":"1","q50130":"1"},{"q50387":"1","q50388":"3","q50389":"0","q50390":"0","q50391":"3"},{"q50490":"2","q50491":"1","q50492":"1","q50493":"1","q50499":"0"},{"q50515":"0","q50522":"2","q50523":"2","q50524":"3","q50525":"1","q50526":"0","q50527":"0","q50528":"2","q50514":["0","1","2","3"],"q50529":"2"},
{"q51413":"0","q51414":"1","q51415":"0","q51416":"1","q51417":"1","q51418":["0","3"],"q51419":"2","q51420":"1","q51421":"1","q51422":"2","q51423":"1","q51424":"2"}]

kaos = {'q635286': '3', 'q635272': '0', 'q635259': '3', 'q635299': '1', 'q635313': '0', 'q635309': '3', 'q635284': '1',
        'q635269': '3', 'q635238': '3', 'q635304': '2', 'q635308': '0', 'q635311': '1', 'q635274': '1', 'q635243': '3',
        'q635310': '2', 'q635285': '2', 'q635312': '1', 'q635244': '0', 'q635298': '0', 'q635278': '2', 'q635240': '1',
        'q635315': '2', 'q635306': '3', 'q635300': '1', 'q635294': '0', 'q635303': '3', 'q635258': '2', 'q635245': '1',
        'q635263': '1', 'q635257': '0', 'q635283': '0', 'q635297': '3', 'q635314': '0', 'q635249': '2', 'q635271': '1',
        'q635293': '1', 'q635252': '2', 'q635260': '2', 'q635265': '2', 'q635267': '1', 'q635305': '3', 'q635261': '3',
        'q635307': '1', 'q635242': '2', 'q635262': '1', 'q635251': '1', 'q635256': '3', 'q635248': '1', 'q635264': '3',
        'q635266': '2'}

class MySignals(QObject):
    #定义信号
    loading = pyqtSignal(str)
    inpuyt_error = pyqtSignal()
    close = pyqtSignal()
    zs=pyqtSignal(list)
    yzm=pyqtSignal(str)
    yzm_error = pyqtSignal()
    get_jd=pyqtSignal(int,int)
    text_print = pyqtSignal(str)

class File():  # 文件的读写
    def __init__(self):
        pass
    def readini(self, section, key):  # 读取
        try:
            conf = configparser.ConfigParser()
            conf.read('.//conf.ini', encoding='utf-8')
            url = conf.get(section, key)
            return url
        except:
            url = ""
            return None



    def witerini(swlf, dictionary):  # 节（section），键（key），值（value） //覆写
        conf = configparser.ConfigParser()
        for section, i in dictionary.items():
            conf.add_section(section)  # 添加section(节)
            for key, value in i.items():
                conf.set(section, key, value)
        conf.write(open('.//conf.ini', "w", encoding="utf-8"))  # 删除原文件重新写入
        # 使用    c={"1":{"efqw":"efq"},"wrvw":{"2ef":"2efqf"}}  //节的值必须为string

class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self ,MainWindow ,parent=None):
        super(TrayIcon, self).__init__(parent)
        self.ui = MainWindow
        self.createMenu()

    def createMenu(self):
        self.menu = QtWidgets.QMenu()
        self.showAction1 = QtWidgets.QAction("启动", self, triggered=self.show_window)
        self.showAction2 = QtWidgets.QAction("设置", self ,triggered=self.showMsg)
        self.quitAction = QtWidgets.QAction("退出", self, triggered=self.quit)

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

        # 设置图标
        self.setIcon(QtGui.QIcon("./img/ard.ico"))
        self.icon = self.MessageIcon()

        # 把鼠标点击图标的信号和槽连接
        self.activated.connect(self.onIconClicked)

    def showMsg(self):
        self.showMessage("通知", "暂时没有设置", self.icon)

    def show_window(self):
        # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
        self.ui.showNormal()
        self.ui.activateWindow()


    def quit(self):
        QtWidgets.qApp.quit()

    # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3:
            # self.showMessage("Message", "skr at here", self.icon)
            if self.ui.isMinimized() or not self.ui.isVisible():
                # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
                self.ui.showNormal()
                self.ui.activateWindow()
                # self.ui.setWindowFlags(QtCore.Qt.Window)
                self.ui.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
                self.ui.show()
            else:
                # 若不是最小化，则最小化
                self.ui.showMinimized()
                self.ui.setWindowFlags(QtCore.Qt.SplashScreen)
                self.ui.show()
                # self.ui.show()

#全局对象
ms = MySignals()        #实例化对象
file=File()

def getTs():
    return int(time.time() * 1000)

class thinklpool():  # 线程池管理类
    def __init__(self, raw):
        self.pool = ThreadPoolExecutor(max_workers=raw)
        # future1 = pool.submit(action, 50)  #提交线程到线程池

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.desktop = QApplication.desktop()       #获取当前显示器分辨率
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        # print(self.height)
        # print(self.width)
        # if (self.width==2560):
        #     Form.resize(440, 270)
        # else:
        #     Form.resize(330, 202)
        Form.resize(440, 270)       #绝对定位没做适配
        Form.setEnabled(True)
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        Form.setStyle(QStyleFactory.create("Windows"))
        Form.activateWindow()
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(174, 200, 110, 40))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 72, 240, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 130, 240, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 50, 72, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 110, 81, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 10, 81, 21))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_visit = QtWidgets.QPushButton(self.layoutWidget)
        self.left_visit.setText("")
        self.left_visit.setObjectName("left_visit")
        self.horizontalLayout.addWidget(self.left_visit)
        self.left_close = QtWidgets.QPushButton(self.layoutWidget)
        self.left_close.setText("")
        self.left_close.setObjectName("left_close")
        self.horizontalLayout.addWidget(self.left_close)
        self.left_out = QtWidgets.QPushButton(self.layoutWidget)
        self.left_out.setText("")
        self.left_out.setObjectName("left_out")
        self.horizontalLayout.addWidget(self.left_out)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(110, 170, 91, 19))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "无名"))
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        pe = QPalette()
        Form.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色
        # pe.setColor(QPalette.Window, QColor(43,115,175))  # 设置背景色
        Form.setPalette(pe)
        self.pushButton.setText(_translate("Form", "LOGIN"))
        self.label.setText(_translate("Form", "UESRNAME"))
        self.label_2.setText(_translate("Form", "PASSWORD"))
        self.checkBox.setText(_translate("Form", "记住密码"))
        self.left_out.setFixedSize(20,20)
        self.left_close.setFixedSize(20,20)
        self.left_visit.setFixedSize(20,20)
        self.left_out.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:10px;}QPushButton:hover{background:red;}''')
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:10px;}QPushButton:hover{background:yellow;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:10px;}QPushButton:hover{background:#a6eca6;}''')
        self.left_close.clicked.connect(Form.showMinimized)  # 最小化窗口
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

class MainUi(QtWidgets.QMainWindow):
    def __init__(self,lisg):
        super().__init__()
        self.jdx = {}
        self.init_ui()
        self.jd(lisg)
        self.tt=TrayIcon(self)
        ms.get_jd.connect(self.xds)
        ms.text_print.connect(self.print_t)
        self.left_visit.clicked.connect(self.show_visit)
        self.left_out.clicked.connect(self.gb)

    def show_visit(self):
        pass
    def gb(self):
        self.setVisible(False)
        self.tt.show()

    def print_t(self,text):
        self.TextBrowser.append(text)
        self.TextBrowser.ensureCursorVisible()

    def xds(self,num,ist):
        self.jdx[num].setValue(ist)

    def jd(self,listc):
        le=len(listc)
        self.num=[]
        self.name=[]
        for i in listc:
            self.num.append(i[0])
            self.name.append(i[1])
        print(self.name)
        print(self.num)
        for i in self.num:
            print(i)
            self.jd_layout = QtWidgets.QHBoxLayout()  # 创建主部件的网格布局
            self.text = QtWidgets.QLabel(self.name[i-1])         #name
            self.jdx[i] = QtWidgets.QProgressBar()
            self.jdx[i].setProperty("value", 0)
            # self.jd[i].setObjectName("")
            self.jd_layout.addWidget(self.text)
            self.jd_layout.addWidget(self.jdx[i])
            self.main_layout.addLayout(self.jd_layout)
        ms.close.emit()


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标
            # print(self.m_Position)

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def init_ui(self):
        pe = QPalette()
        self.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色
        # pe.setColor(QPalette.Window, QColor(43,115,175))  # 设置背景色
        self.setPalette(pe)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.setInputMethodHints(QtCore.Qt.ImhNone)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setFixedSize(600,500)
        self.activateWindow()

        print(self.height)
        print(self.width)
        #创建主部件
        self.main_widget = QtWidgets.QWidget(self)  # 创建窗口主部件
        self.main_widget.setFixedSize(500,270)
        self.main_layout = QtWidgets.QVBoxLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.main_layout.setSpacing(10)          #控件间距
        self.main_widget.setStyleSheet('''*{background-color:#a8edea;}''')
        self.main_widget.move(50,80)
        #头部部件

        self.TextBrowser = QtWidgets.QTextBrowser(self)
        self.TextBrowser.setFixedSize(500, 130)
        self.TextBrowser.move(50, 360)


        self.left_username = QtWidgets.QLabel(" 草率的看板",self)
        self.left_username.setObjectName('username')
        self.left_out = QtWidgets.QPushButton(self)
        self.left_out.setObjectName('left_out')
        self.left_out.setFixedSize(20,20)
        self.left_close = QtWidgets.QPushButton(self) # 最小化
        self.left_close.setFixedSize(20,20)
        self.left_close.setObjectName('left_close')
        self.left_close.clicked.connect(self.showMinimized)   # 点击按钮之后关闭窗口
        self.left_visit = QtWidgets.QPushButton(self) # 帮助
        self.left_visit.setFixedSize(20,20)
        self.left_visit.setObjectName('left_visit')

        #头部按钮布局位置
        self.left_username.move(1,1)
        self.left_out.move(570, 8)
        self.left_close.move(545, 8)
        self.left_visit.move(520, 8)


        # self.text_z.setValue(24)
        #qss
        self.left_username.setStyleSheet('''QPushButton{ text-align:left;padding-left:30px;color:#ffffff;font-size:16px;}''')
        self.left_out.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:10px;}QPushButton:hover{background:red;}''')
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:10px;}QPushButton:hover{background:yellow;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:10px;}QPushButton:hover{background:green;}''')

class XX(Ui_Form):
    def __init__(self):
        super().__init__()
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            # self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标
            # print(self.m_Position)

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

class login():
    def __init__(self,use,password):    #构造函数

        self.use=use
        self.password=password
        # self.driver = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()          #设置浏览器后台运行
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://www.cqooc.net/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def xuan_ke(self):
        self.driver.get("http://www.cqooc.net/course/online/detail?id=334568696")
        self.driver.find_element_by_id("join-btn").click()
        pass

    def cole(self):
        self.driver.quit()

    def join(self):            #输入密码登录函数
        self.driver.find_element_by_name("username").send_keys(self.use)
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(0.3)
        self.driver.find_element_by_id("loginBtn").click()
        return

    def tit_jmp(self):           #判断页面是否跳转，跳转返回Turn，没有返回，Flase
        title=self.driver.title
        da_if = True
        if title!="登录":
            return da_if
        else:
            da_if= False
            return da_if

    def ver_code(self):         #判断是否有验证码，有，返回True，没有返回False
        da_if = True
        try:
            t = self.driver.find_element_by_class_name("verify-code").get_attribute('data-key')
            return da_if
        except:
            da_if= False
            return da_if

    def decide_pop(self):           #判断是否有弹窗，有，返回弹窗头，没有,返回False
        pop = self.driver.find_element_by_id("dialog_overlay").get_attribute('style')
        da_if = False
        try:
            if pop == "visibility: visible;":
                title = self.driver.find_element_by_id("dialog_title").text
                return title
            else:
                return da_if
        except:
            return da_if

    def qa_code(self,i):             #截取二维码并保存
        code_element = self.driver.find_element_by_class_name("verify-code")
        self.driver.get_screenshot_as_file("..\\img\\img{0}_full.png".format(i))
        left = code_element.location_once_scrolled_into_view['x'] + 604
        top = code_element.location_once_scrolled_into_view['y'] + 152
        right = 180 + left
        height = 70 + top
        print(left, top, right, height)
        im = Image.open("..\\img\\img{0}_full.png".format(i))
        img = im.crop((left, top, right, height))  # 截取验证码图片保存
        save_res = img.save("..\\img\\img{0}.png".format(i))
        return save_res

    def qa_pip(i):
        img = Image.open("..\\img\\img{0}.png".format(i))
        img = img.convert('L')  # P模式转换为L模式(灰度模式默认阈值127)
        count = 127  # 设定阈值
        table = []
        for i in range(256):
            if i < count:
                table.append(0)
            else:
                table.append(1)
        img = img.point(table, '1')
        img.save("..\\img\\img{0}deal.png".format(i))  # 保存处理后的验证码

    def get_cookie(self):
        info = self.driver.get_cookie('xsid')
        cookie = info["value"]
        return cookie

    def get_src(self):
        get_src=self.driver.find_element_by_css_selector(".verify-code img").get_attribute('src')
        src=get_src[24:]
        imgdata = base64.b64decode(src)
        path='./src.jpg'
        file = open(path, 'wb')
        file.write(imgdata)
        file.close()
        return path

    def ewm_put(self,ss):
        self.driver.find_element_by_name("verify").send_keys(ss)
        self.driver.find_element_by_id("loginBtn").click()
        time.sleep(2)
        if self.tit_jmp() == False:  # 检测是否跳转
            return False
        return True

class windos():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ex = XX()
        self.ui=Ui_Form()
        self.ui.setupUi(self.ex)
        self.ex.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #托盘对象
        self.ti = TrayIcon(self.ex)
        # 设置事件触发
        self.ui.left_visit.clicked.connect(self.show_visit)
        self.ui.pushButton.clicked.connect(self.main)
        self.ui.left_out.clicked.connect(self.gb)
        #槽函数绑定
        ms.inpuyt_error.connect(self.inpuyt_error)
        ms.close.connect(self.clos)
        ms.zs.connect(self.show_zdy)
        ms.yzm.connect(self.show_YZM)
        ms.yzm_error.connect(self.yzm_error)
        #初始化事件
        use=file.readini("zh","use")
        password=file.readini("zh","password")
        state=file.readini("zh","state")
        self.ui.lineEdit.setText(use)
        self.ui.lineEdit_2.setText(password)
        if state == "True":
            self.ui.checkBox.setChecked(True)

    def gb(self):
        reply = QtWidgets.QMessageBox.question(self.ui,'退出提示',"是否最小化至托盘？",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.ex.setVisible(False)
            self.ti.show()
        else:
            self.ex.close()  # 关闭并退出托盘对象

    def echo(self, listc):
        '''显示对话框返回值'''
        print(listc)
        thread = Thread(target=show_main,args=(listc,))
        thread.setDaemon(True)
        thread.start()
        appo=thinklpool(1)
        ms.text_print.emit("开始刷视频")
        for i in listc:
            appo.pool.submit(mode_2_run, self.cookie,i[0])
        appo.pool.submit(mode_1_run,self.cookie)
        ms.close.emit()

    def loading(self,text):
        self.ui.pushButton.setText(text)

    def loging(self,use,password):
        self.state=False
        while True:
            time.sleep(1)
            print(self.state)
            try:
                if self.state == "ss":
                    break
                if self.state ==True:
                    if self.longin.tit_jmp() == True:  # 检测是否跳转
                        print('yes')
                        self.cookie = self.longin.get_cookie()  # 获取网页的cookie值
                        print(self.cookie)
                        time.sleep(1)
                        self.longin.cole()
                        a = AutoCompleteOnlineCourse(self.cookie)
                        thread = Thread(target=a.zs)
                        thread.setDaemon(True)
                        thread.start()
                        break
                if self.state ==False:
                    self.longin = login(use, password)
                    self.longin.join()
                    time.sleep(2)
                    if self.longin.tit_jmp() == True:   # 检测是否跳转
                        print('yes')
                        self.cookie = self.longin.get_cookie()  # 获取网页的cookie值
                        print(self.cookie)
                        time.sleep(1)
                        self.longin.cole()
                        a = AutoCompleteOnlineCourse(self.cookie)
                        thread = Thread(target=a.zs)
                        thread.setDaemon(True)
                        thread.start()
                        break
                    else:
                        tc = self.longin.decide_pop()
                        if self.longin.ver_code() == True and tc == False:  # 检测验证码
                            path = self.longin.get_src()
                            ms.yzm.emit(path)
                            self.state="yzm"
                            continue
                        if tc != False:  # 检测弹窗
                            if tc == "提示":  # 验证码
                                if self.longin.ver_code() == True:  # 检测验证码
                                    path = self.longin.get_src()
                                    ms.yzm.emit(path)
                                    self.state = "yzm"
                                    continue
                            if tc == "Error":  # 密码错误
                                ms.inpuyt_error.emit()
                                self.longin.cole()
                                break
                        else:
                            self.longin.driver.find_element_by_id("loginBtn").click()
            except:
                self.longin.cole()

    def rwm_tit(self,path):
        self.ssin = yzm_win(path)
        self.ssin.show()
        self.ssin.before_close_signal.connect(self.ecch)  # 关闭信号

    def ecch(self,str):
        c=self.longin.ewm_put(str)
        if c == True:
            self.state=True
        else:
            tc = self.longin.decide_pop()
            if tc != False:  # 检测弹窗
                if tc == "提示":  # 验证码
                    ms.yzm_error.emit()
                    self.longin.cole()
                    self.state = "ss"
                if tc == "Error":  # 密码错误
                    ms.inpuyt_error.emit()
                    self.longin.cole()
                    self.state = "ss"

    def show_zdy(self,ss):
        self.window2 = MyWindow2(ss)  # 自定义窗口
        self.window2.show()
        self.window2.before_close_signal.connect(self.echo)    #关闭信号

    def cc(self):
        QMessageBox.question(self.ui, '提示', "账户和密码不能为空", QMessageBox.Yes)

    def inpuyt_error(self):
        QMessageBox.question(self.ui, 'Error', "密码错误", QMessageBox.Yes)
        self.ui.lineEdit_2.setText("")
        self.ui.pushButton.setText("重新登陆")
    def yzm_error(self):
        QMessageBox.question(self.ui, 'Error', "验证码错误", QMessageBox.Yes)

    def show_visit(self):
        # lisdcc=[[1, '职场交际英语'], [2, 'C程序设计（第六次开课）'], [3, '高等数学Ⅱ（第四次开课）'], [4, '计算机组装与维护（第五次开课）']]
        # thread = Thread(target=show_main,args=(lisdcc,))
        # thread.setDaemon(True)
        # thread.start()
        # ms.close.emit()
        # # self.show_YZM("./src.jpg")
        # # self.ssin = yzm_win('./src.jpg')
        # # self.ssin.before_close_signal.connect(self.ecch)  # 关闭信号
        QMessageBox.question(self.ui, '帮助', "这里没有帮助", QMessageBox.Yes)

    def show_YZM(self,path):
        self.ssin = yzm_win(path)
        self.ssin.before_close_signal.connect(self.ecch)  # 关闭信号
        # text, okPressed = QInputDialog.getText(self.ui, "验证码", "验证码：", QLineEdit.Normal, "")
        # if okPressed and text != '':
        #     print(text)

    def clos(self):
        self.ex.close()

    def main(self):
        use=self.ui.lineEdit.text()
        password=self.ui.lineEdit_2.text()
        if use != "" and password != "":
            print(use,password)
            if self.ui.checkBox.isChecked()==True:
                file.witerini({"zh":{"use":use,"password":password,"state":"True"}})
            else:
                file.witerini({"zh": {"use": "", "password": "","state":"False"}})
            self.ui.pushButton.setText("登录ing..")
            thread = Thread(target=self.loging,args=(use,password))
            thread.setDaemon(True)
            thread.start()
            # thread.join()
        else:
            self.cc()

class MyWindow2(QWidget):
    '''自定义窗口'''
    before_close_signal = pyqtSignal(list)  # 自定义信号（list类型）
    def __init__(self,ss):
        super().__init__()
        self.but = {}
        self.a = ss
        self.le=len(self.a)
        self.setWindowTitle('选择课程(可多选)')
        self.resize(300, 150)
        layout_main=QVBoxLayout(self)
        layout = QHBoxLayout()
        layout_main.addLayout(layout)
        createVar = locals()
        for i in range(0,self.le):
            self.but[i]=QCheckBox(text=self.a[i])
            layout.addWidget(self.but[i])

        btn=QPushButton("确认")
        layout_main.addWidget(btn)
        btn.clicked.connect(self.btn)
        # print(var2)
    def btn(self):
        cc=[]
        for i in range(0,self.le):
            zz=[]
            c=self.but[i].isChecked()
            if c ==True :
                zz.append(i+1)
                zz.append(self.a[i])
            else:
                continue
            cc.append(zz)
        self.before_close_signal.emit(cc)  # 发送信号，带参数 888
        self.close()  # 然后窗口关闭

    # 默认关闭事件
    def closeEvent(self, e):
        self.close()  # 然后窗口关闭

class yzm_win(QWidget):
    '''自定义窗口'''
    before_close_signal = pyqtSignal(str)  # 自定义信号（int类型）
    def __init__(self,path):
        super().__init__()
        self.but = {}
        self.path = path
        self.setWindowTitle('请输入二维码')
        self.resize(300, 140)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        layout_main=QVBoxLayout(self)
        layout = QHBoxLayout()
        layout_main.addLayout(layout)
        self.box1_pix = QtWidgets.QLabel()
        self.box1_pix.setObjectName('box1_pix')
        self.box1_pix.setPixmap(QPixmap(path))
        self.box1_pix.setFixedSize(160, 66)
        self.box1_pix.setScaledContents(True)
        self.but=QLineEdit("")
        self.show()

        layout.addWidget(self.box1_pix)
        layout.addWidget(self.but)

        btn=QPushButton("确认")
        layout_main.addWidget(btn)
        btn.clicked.connect(self.btn)
    def btn(self):
        self.cc=self.but.text()
        self.before_close_signal.emit(self.cc)  # 发送信号，带参数 888
        self.close()  # 然后窗口关闭
    # def show(self) -> None:
    #     return self.cc

class AutoCompleteOnlineCourse():
    def __init__(self,cookie,mue=None):
        self.cookie=cookie

        if self.cookie == '':
            print("请添加xsid")
            exit(0)
        # headers
        session = requests.Session()
        session.headers['Cookie'] = 'player=1; xsid=' + self.cookie
        # session.headers['Connection'] = 'close'
        session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        session.headers['Host'] = 'www.cqooc.com'
        session.keep_alive = False
        self.Session = session
        self.CompleteCourse = None
        self.courseId = None
        self.courseDes = None
        self.mue=mue

    def mm(self):
        atuo = Atuoabout(self.cookie)
        try:
            atuo.big_ti("作答")
            print("fe")
        except:
            ms.text_print.emit("自动答题失败")
            # file().wicth_txt_test("schedule", "{}\t{}自动答题失败".format(istime(), self.num))
        time.sleep(2)
        try:
            atuo.keti()
            print("fe")
        except:
            ms.text_print.emit("自动课后题失败")
            # file().wicth_txt_test("schedule", "{}\t{}自动课后题失败".format(istime(), self.num))
        time.sleep(2)
        try:
            atuo.kao_s()
            print("fe")
        except:
            ms.text_print.emit("自动考试失败")
            # file().wicth_txt_test("schedule", "{}\t{}自动考试失败".format(istime(), self.num))
        # file().wicth_txt_test("schedule","{}\t{}运行结束".format(istime(),self.num))
        # file().wicth_txt_close("diary","{}".format(self.num))

    def get(self, url, headers=None):
        while True:
            try:
                return self.Session.get(url, headers=headers)
            except:
                continue

    def post(self, url, json=None, headers=None):
        while True:
            try:
                return self.Session.post(url, json=json, headers=headers)
            except:
                continue

    def zs(self):
        info = self.getInfomation()
        try:
            print('Login ID:', info['username'])
        except:
            print("xsid有误，请检查！")
            return
        self.ownerId = info['id']
        self.username = info['username']
        zx=[]
        for index, i in enumerate(self.getCourseInfo()['data']):
            print("{}、{}".format(index + 1, i['title']))
            zx.append(i['title'])
        ms.zs.emit(zx)
        return zx

    def main(self) -> None:
        info = self.getInfomation()
        try:
            print('Login ID:', info['username'])
        except:
            print("xsid有误，请检查！")
            return
        self.ownerId = info['id']
        self.username = info['username']

        courseData = []
        for index, i in enumerate(self.getCourseInfo()['data']):
            print("{}、{}".format(index + 1, i['title']))
            courseData.append({
                "title": i['title'],
                "parentId": i['id'],
                "courseId": i['courseId']
            })
        while True:
            try:
                id = self.mue
                self.title = courseData[int(id) - 1]['title']
                break
            except:
                print("输入有误，请重新输入！")
                continue
        self.parentId = courseData[int(id) - 1]['parentId']
        self.courseId = courseData[int(id) - 1]['courseId']
        print("\n已选择 {}".format(self.title))
        while True:
            print("\n开始模拟观看网课\n")
            self.CompleteCourse = self.getCompleteCourse()
            self.getCourseDes()
            self.startLearnCourse()
            break
        # self.mm()

    def getCourseDes(self):
        # 课程章节名
        self.Session.headers['Referer'] = f'http://www.cqooc.com/my/learn/mooc/structure?id={self.courseId}'
        courseDes = {}
        res = self.get(
            f'http://www.cqooc.com/json/chapters?limit=200&start=1&sortby=selfId&status=1&courseId={self.courseId}&select=id,title,level,selfId,parentId&ts={getTs()}')
        for i in res.json()['data']:
            courseDes[i['id']] = i['title']
        self.courseDes = courseDes

    def getInfomation(self) -> json:
        """
        获取基本信息
        :return:
        """
        return self.get('http://www.cqooc.com/user/session?xsid=' + self.cookie).json()

    def getCourseInfo(self) -> json:
        """
        获取课程信息
        :return:
        """
        self.Session.headers['Referer'] = 'http://www.cqooc.com/my/learn'
        return self.get(
            'http://www.cqooc.com/json/mcs?sortby=id&reverse=true&del=2&courseType=2&ownerId={}&limit=10'.format(
                self.ownerId)).json()

    def getCompleteCourse(self) -> list:
        """
        获取已完成小节列表
        :return:
        """
        self.Session.headers['Referer'] = 'http://www.cqooc.com/learn/mooc/progress?id=' + self.courseId
        data = self.get(
            f'http://www.cqooc.com/json/learnLogs?limit=100&start=1&courseId={self.courseId}&select=sectionId&username={self.username}&ts={getTs()}')
        CourseIdList = []
        for i in data.json()['data']:
            CourseIdList.append(i['sectionId'])
        return CourseIdList

    def startLearn(self) -> json:
        self.Session.headers['Referer'] = 'http://www.cqooc.com/learn/mooc/structure?id=' + self.courseId
        return self.post(url='http://www.cqooc.com/account/session/api/login/time', json={
            "username": self.username
        }).json()

    def getLog(self, sectionId) -> json:
        self.Session.headers['Referer'] = 'http://www.cqooc.com/learn/mooc/structure?id=' + self.courseId
        return self.get(
            'http://www.cqooc.com/json/learnLogs?sectionId=' + sectionId + '&username=' + self.username).json()

    def checkProgress(self, courseId, sectionId, chapterId) -> None:
        count = 0
        while True:
            self.Session.headers['Referer'] = 'http://www.cqooc.com/learn/mooc/structure?id=' + courseId

            self.startLearn()
            self.getLog(sectionId)
            time.sleep(20)
            self.startLearn()
            time.sleep(1)

            Log = self.post('http://www.cqooc.com/learnLog/api/add', json={
                "action": 0,
                "category": 2,
                "chapterId": str(chapterId),
                "courseId": str(courseId),
                "ownerId": self.ownerId,
                "parentId": str(self.parentId),
                "sectionId": int(sectionId),
                "username": self.username
            })

            if count <= 2:
                date = 40
            else:
                date = 150

            if Log.json()['msg'] == '已经添加记录' or Log.json()['msg'] == 'No error':
                return
            else:
                time.sleep(date)
                count += 1
                continue

    def startLearnCourse(self):

        sectionList = \
            self.get('http://www.cqooc.com/json/chapter/lessons?courseId=' + self.courseId).json()['data'][0]['body']
        index_t = 0
        # CompleteCourse = self.getCompleteCourse()
        print("已完成小节数: {} ".format(len(self.CompleteCourse)))
        for chapterId, sectionIds in sectionList.items():
            print('章节进度: {}/{}({:.2f}%) \t当前: {}'.format(index_t + 1, len(sectionList.items()),
                                                         ((float((index_t + 1) / len(sectionList.items()))) * 100),
                                                         self.courseDes.get(chapterId)))
            index_t += 1
            ms.get_jd.emit(self.mue,int(((float((index_t + 1) / len(sectionList.items()))) * 100)))
            for index, sectionId in enumerate(sectionIds):
                print('\t小节进度: %d/%d(%.2f%%)' % (
                    index + 1, len(sectionIds), (float((index + 1) / len(sectionIds)) * 100)), end='')
                if sectionId in self.CompleteCourse:
                    print('\t已完成，跳过!')
                    continue
                print('\t成功!')
                self.checkProgress(self.courseId, sectionId, chapterId)

class Atuoabout():
    def __init__(self,cookie):
        self.cookieXsidUser = cookie
        session = requests.Session()
        session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        # self.session.headers['Connection'] = 'close'
        session.headers['Connection'] = 'close'
        session.headers['Host'] = 'www.cqooc.com'
        session.headers['cookie'] = 'xsid={}; player=1'.format(self.cookieXsidUser)
        session.headers['Cache-Control'] = 'max-age=0'
        session.headers['UContent-Type'] = "text/html;charset=UTF-8"
        self.Session = session
        info = self.get('http://www.cqooc.com/user/session?xsid=' + self.cookieXsidUser).json()
        self.ownerId = info.get("id")
        self.username = info.get("username")
        self.name= self.get(f'http://www.cqooc.com/account/session/api/profile/get?ts={getTs()}').json().get("name")

    def post(self, url, json=None, headers=None, data=None):
        while True:
            try:
                return self.Session.post(url, json=json, headers=headers, data=data)
            except:
                continue

    def get(self, url, json=None, headers=None, data=None):
        while True:
            try:
                return self.Session.get(url, json=json, headers=headers, data=data)
            except:
                continue

    def getid(self):
        response = self.get("http://www.cqooc.net/exam/api/paper/get?examId=5707&ts=1619101597992", headers={
            'Referer': 'http://www.cqooc.net/learn/mooc/exam/do?pid=5707&id=334568696',
        })
        data=response.json().get("data")
        print(data)

    def big_ti(self,text):          #十个大题
        num=["43215","43216","43217","43218","43219","43220","43221","43222","43223","43224"]
        str_x="<p>{}</p>".format(text)
        for i in range(0, 10):
            a = num[i]
            response = self.post('http://www.cqooc.net/task/api/result/add',json=None, headers={
                'Referer': f'http://www.cqooc.net/learn/mooc/task/do?tid={i}&id=334568696',
            }, data=json.dumps({
                "attachment": "",               #固定
                "classId": "",                  #固定
                "content": str_x,
                "courseId": "334568696",        #固定
                "name": self.name,
                "ownerId": self.ownerId,
                "status": "2",                  #固定
                "taskId": a,
                "username": self.username
            }))
            print(i+1,response)

    def tz(self,text):              #发帖子
        str_x="{}".format(text)
        response = self.post('http://www.cqooc.net/json/forums',json=None, headers={
            'Referer': f'http://www.cqooc.net/learn/mooc/forum?id=334568696',
        }, data=json.dumps({
            "category": "1",                #固定
            "voteNum":0,                       #固定
            "commentNum": 0,                    #固定
            "content": "<p>&nbsp;</p>",         #固定
            "courseId": "334568696",            #固定
            "name": self.name,
            "ownerId": self.ownerId,
            "status": "1",                      #固定
            "title": str_x,
            "username": self.username
        }))
        print(response)

    def keti(self):         #隋唐题目
        for i in range(0, 30):
            response = self.post('http://www.cqooc.net/test/api/result/add', headers={
                'Referer': f'http://www.cqooc.net/learn/mooc/testing/do?tid={list_num[i]}&id=334568696&sid=630097&cid=245490&mid=335571474',
            }, data=json.dumps({"ownerId":self.ownerId,
                                "username":self.username,
                                "name":self.name,
                                "paperId":list_num[i],
                                "courseId":"334568696",
                                "answers":list_a[i],
                                "classId":""
                                }))
            print(i,response)
            time.sleep(1)

    def kao_s(self):
        session = requests.Session()
        session.headers[
            'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        # self.session.headers['Connection'] = 'close'
        session.headers['Connection'] = 'keep-alive'
        session.headers['Host'] = 'www.cqooc.com'
        session.headers['cookie'] = 'xsid={}; player=1'.format(self.cookieXsidUser)
        session.headers['Origin'] = 'http://www.cqooc.net'
        session.headers['Content-Length'] = "832"
        response = session.post('http://www.cqooc.net/exam/do/api/submit', headers={
            'Referer': f'http://www.cqooc.net/learn/mooc/exam/do?pid=5707&id=334568696',
        }, data=json.dumps({"ownerId": self.ownerId,
                            "username": self.username,
                            "examId": "5707",
                            "name": self.name,
                            "courseId": "334568696",
                            "answers": kaos,
                            "id": self.kap_id()
                            }))
        print(response)

    def kap_id(self):
        response = self.post('http://www.cqooc.net/exam/api/paper/gen', headers={
            'Referer': f'http://www.cqooc.net/learn/mooc/exam/do?pid=5707&id=334568696',
        }, data=json.dumps({"ownerId": self.ownerId, "username": self.username, "name": self.name, "examId": "5707", "courseId": "334568696"}))

        print(response)
        print(response.json())
        time.sleep(1)
        response1 = self.get('http://www.cqooc.net/exam/api/paper/get?examId=5707&ts=1619104183382', headers={
            'Referer': f'http://www.cqooc.net/learn/mooc/exam/do?pid=5707&id=334568696',}, data=None)
        print(response1)
        ks_id=response1.json().get("data")[0]["id"]
        sss=str(ks_id)
        return sss


def show_login():
    a = windos()
    a.ex.show()
    sys.exit(a.app.exec_())

def show_main(lisg):
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi(lisg)
    gui.show()
    sys.exit(app.exec_())

def main():
    show_login()

def mode_2_run(cookie,num):
    a = AutoCompleteOnlineCourse(cookie, num)
    a.main()
def mode_1_run(cookie):
    ms.text_print.emit("正在刷题")
    a = AutoCompleteOnlineCourse(cookie)
    a.mm()

if __name__ == '__main__':
    # freeze_support()
    main()