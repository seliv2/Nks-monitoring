import a2s
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import webbrowser


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 246)
        MainWindow.setMaximumSize(QtCore.QSize(968, 246))
        MainWindow.setMinimumSize(QtCore.QSize(968, 246))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 60, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.classic)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 20, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.awp)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 100, 131, 31))
        self.pushButton_4.clicked.connect(self.openawp)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 140, 131, 31))
        self.pushButton_5.clicked.connect(self.openclassik)
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(180, 0, 771, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openawp(self):
        webbrowser.open('steam://connect/5.159.111.205:27016')
    def openclassik(self):
        webbrowser.open('steam://connect/5.159.111.205:27015')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Приложение NKS"))
        self.pushButton_2.setText(_translate("MainWindow", "Classik"))
        self.pushButton_3.setText(_translate("MainWindow", "Awp server"))
        self.pushButton_4.setText(_translate("MainWindow", "Connect awp"))
        self.pushButton_5.setText(_translate("MainWindow", "connect Classik"))

    def awp(self, MainWindow):
        address = ("5.159.111.205", 27016)
        nick = a2s.players(address)
        servername = a2s.info(address).server_name
        map = str(a2s.info(address).map_name)
        online = str(a2s.info(address).player_count)
        max = str(a2s.info(address).max_players)
        self.textBrowser.setText(servername + "\n" + map.strip("workshop,/,1,2,3,4,5,6,7,8,9,0") + "\n" + online + "/" + max)
        for i in nick:
            if not i.name:
                i.name = "Неизвестный ник"
            times = round(i.duration)
            time = str(datetime.timedelta(seconds = times))
            names = i.name
            self.textBrowser.append("\n" + names + " " + time)

    def classic(self, MainWindow):
        address = ("5.159.111.205", 27015)
        nick = a2s.players(address)
        servername = a2s.info(address).server_name
        map = str(a2s.info(address).map_name)
        online = str(a2s.info(address).player_count)
        max = str(a2s.info(address).max_players)
        self.textBrowser.setText(servername + "\n" + map.strip("workshop,/,1,2,3,4,5,6,7,8,9,0") + "\n" + online + "/" + max)
        for f in nick:
            if not f.name:
                f.name = "Неизвестный ник"
            times = round(f.duration)
            time = str(datetime.timedelta(seconds=times))
            names = f.name
            self.textBrowser.append("\n" + names + " " + time)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

