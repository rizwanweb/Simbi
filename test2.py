# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import csv
import time

msg = 'Hello World'


class Ui_MainWindow(object):

    inbox = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 82))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.lblUsername = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblUsername.setTextFormat(QtCore.Qt.AutoText)
        self.lblUsername.setObjectName("lblUsername")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.lblUsername)
        self.txtUsername = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtUsername.setObjectName("txtUsername")
        self.txtUsername.setText("noodzakelijkonline@gmail.com")

        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.txtUsername)
        self.lblPassword = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblPassword.setObjectName("lblPassword")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.lblPassword)
        self.txtPassword = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPassword.setObjectName("txtPassword")

        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.txtPassword)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 10, 221, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lblCounter = QtWidgets.QLabel(self.centralwidget)
        self.lblCounter.setGeometry(QtCore.QRect(370, 50, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.lblCounter.setFont(font)
        self.lblCounter.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lblCounter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lblCounter.setText("")
        self.lblCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCounter.setObjectName("lblCounter")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 100, 581, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.statusImage = QtWidgets.QGraphicsView(self.centralwidget)
        self.statusImage.setEnabled(False)
        self.statusImage.setGeometry(QtCore.QRect(370, 130, 221, 121))
        self.statusImage.setObjectName("statusImage")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 260, 221, 23))
        self.label_4.setObjectName("label_4")

        self.txtNextMessage = QtWidgets.QLabel(self.centralwidget)
        self.txtNextMessage.setGeometry(QtCore.QRect(370, 290, 221, 51))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.txtNextMessage.setFont(font)
        self.txtNextMessage.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.txtNextMessage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.txtNextMessage.setText("")
        self.txtNextMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.txtNextMessage.setObjectName("txtNextMessage")

        self.txtMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.txtMessage.setGeometry(QtCore.QRect(79, 170, 271, 171))
        self.txtMessage.setMinimumSize(QtCore.QSize(200, 0))
        self.txtMessage.setObjectName("txtMessage")
        self.txtMessage.setText(msg)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 63, 21))
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 182, 37))
        self.label_2.setObjectName("label_2")

        self.txtTime = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTime.setGeometry(QtCore.QRect(200, 130, 151, 37))
        self.txtTime.setObjectName("txtTime")
        self.txtTime.setText("60")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 350, 581, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btnStart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnStart.setObjectName("btnStart")

        self.horizontalLayout.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)

        self.btnClose = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.btnClose.clicked.connect(self.exitApp)  # Exit Application

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopt = QtWidgets.QAction(MainWindow)
        self.actionCopt.setObjectName("actionCopt")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtUsername, self.txtPassword)
        MainWindow.setTabOrder(self.txtPassword, self.txtTime)
        MainWindow.setTabOrder(self.txtTime, self.btnStart)
        MainWindow.setTabOrder(self.btnStart, self.btnStop)
        MainWindow.setTabOrder(self.btnStop, self.btnClose)
        MainWindow.setTabOrder(self.btnClose, self.statusImage)
        MainWindow.setTabOrder(self.statusImage, self.txtMessage)

        # Load number of previous entries from csv file
        counter = self.loadPreviousRequestSent()
        print(counter)
        self.lblCounter.setText(str(counter))

        # Disable stop Button
        self.btnStop.setEnabled(False)

        # Run function
        self.btnStart.clicked.connect(self.runApp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simbi"))
        self.lblUsername.setText(_translate("MainWindow", "Username:"))
        self.lblPassword.setText(_translate("MainWindow", "Password:"))
        self.label.setText(_translate("MainWindow", "Already Sent Messages"))
        self.label_4.setText(_translate(
            "MainWindow", "Time Until Next Message"))
        self.label_3.setText(_translate("MainWindow", "Message"))
        self.label_2.setText(_translate(
            "MainWindow", "Interval Time (in Minutes)"))
        self.btnStart.setText(_translate("MainWindow", "Run"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.btnClose.setText(_translate("MainWindow", "Exit"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save a file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopt.setText(_translate("MainWindow", "Copt"))
        self.actionCopt.setStatusTip(_translate("MainWindow", "Copy a file"))
        self.actionCopt.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste a file"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate(
            "MainWindow", "Create a new file"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

    # Run Function

    def runApp(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        # print(username, password)
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)
        driver.get('https://simbi.com/')

        login_url = driver.find_element(
            By.XPATH, '/html/body/nav[2]/div/div[3]/a[3]')
        login_url.click()

        txtUsername = driver.find_element(By.ID, 'user_email')
        txtPassword = driver.find_element(By.ID, 'user_password')
        btnLogin = driver.find_element(By.NAME, 'commit')

        txtUsername.send_keys(username)
        txtPassword.send_keys(password)
        btnLogin.click()
        sleep(3)

        page_number = 1
        while page_number < 150:
            driver.get(f'https://simbi.com/requests?page={page_number}')

            cards = driver.find_elements(By.CLASS_NAME, 'click-link')

            request_links = []

            # Find already sent masseges if any
            for c in cards:
                post_link = c.get_attribute('href') in (
                    item for sublist in self.inbox for item in sublist)

                if post_link:
                    print("Visited")
                else:
                    request_links.append(c.get_attribute('href'))

            print(len(request_links), "links")
            if len(request_links) > 0:
                for link in request_links:
                    driver.get(link)
                    sleep(2)
                    request_title = driver.find_element(
                        By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div[1]/h2[1]')
                    # sleep(1)
                    user_title = driver.find_element(
                        By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/a/h4')
                    # sleep(1)
                    user_request = driver.find_element(
                        By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div[4]/p')
                    # sleep(1)
                    data = [user_title.text, request_title.text,
                            link, user_request.text]

                    if data in self.inbox:
                        print("Messege already sent")
                    else:
                        btnConversation = driver.find_element(
                            By.ID, 'start-conversation-btn')
                        btnConversation.click()

                        msg = f"Hello {user_title.text},\n I came across you request {request_title.text}\n I think i can help by finding the right Simbi candidate for you to help you with your request. Would you be interested in that ?\n For more information, here is my Simbi service:\n {settings.service_URL}\n Looking forward to hearing from you\n ~ {settings.name}"
                        sleep(2)

                        inquiry_box = driver.find_element(
                            By.NAME, 'inquiry_text')
                        inquiry_box.send_keys(msg)
                        sleep(1)
                        btnCancel = driver.find_element(
                            By.CSS_SELECTOR, 'body > div.modal.fade.brand-modal.v-middle.inquiry-modal.in > div > div > div > div.flex.between > button.btn.btn-wide-xs.btn-default')
                        btnCancel.click()

                        with open('inbox.csv', 'a', encoding="utf-8") as fin:
                            writer = csv.writer(fin)
                            writer.writerow(data)

                    driver.get(
                        f'https://simbi.com/requests?page={page_number}')
                    sleep(2)
            else:
                pass
            page_number += 1

    # Exit Application Function
    def exitApp(self):
        sys.exit(self.app.exec_())

    # Load entries from inbox.csv
    def loadPreviousRequestSent(self):
        with open('inbox.csv', 'r') as fil:
            file_reader = csv.reader(fil)
            for row in file_reader:
                self.inbox.append(row)
        return len(self.inbox)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
