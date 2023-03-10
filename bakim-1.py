# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bakim-1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import datetime

        
x_date = datetime.now()
guncel_tar = x_date.strftime("%d/%m/%Y")
conn = sqlite3.connect('bakim.db')
cursor = conn.cursor()




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.daily_works = QtWidgets.QListWidget(self.centralwidget)
        self.daily_works.setGeometry(QtCore.QRect(30, 80, 381, 521))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.daily_works.setFont(font)
        self.daily_works.setObjectName("daily_works")
        
        query = 'select makine_adi from makine where bakim_tar=?'
        cursor.execute(query,(guncel_tar,))
        results = cursor.fetchall()
        for result in results:
            self.daily_works.addItem(str(result[0]))
            
        self.gunluk_label = QtWidgets.QLabel(self.centralwidget)
        self.gunluk_label.setGeometry(QtCore.QRect(30, 30, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gunluk_label.setFont(font)
        self.gunluk_label.setTextFormat(QtCore.Qt.AutoText)
        self.gunluk_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gunluk_label.setObjectName("gunluk_label")
        self.bakim_button = QtWidgets.QPushButton(self.centralwidget)
        self.bakim_button.setGeometry(QtCore.QRect(650, 480, 221, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bakim_button.setFont(font)
        self.bakim_button.setObjectName("bakim_button")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(450, 80, 641, 151))
        self.textEdit.setObjectName("textEdit")
        self.not_label = QtWidgets.QLabel(self.centralwidget)
        self.not_label.setGeometry(QtCore.QRect(450, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.not_label.setFont(font)
        self.not_label.setObjectName("not_label")
        self.kullanilan_urun_label = QtWidgets.QLabel(self.centralwidget)
        self.kullanilan_urun_label.setGeometry(QtCore.QRect(450, 250, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.kullanilan_urun_label.setFont(font)
        self.kullanilan_urun_label.setObjectName("kullanilan_urun_label")
        self.urun_list = QtWidgets.QComboBox(self.centralwidget)
        self.urun_list.setGeometry(QtCore.QRect(450, 300, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.urun_list.setFont(font)
        self.urun_list.setObjectName("urun_list")
        self.adet_label = QtWidgets.QLabel(self.centralwidget)
        self.adet_label.setGeometry(QtCore.QRect(730, 260, 91, 21))
        
        query_parca='select parca_adi from parca'
        cursor.execute(query_parca)
        parcalar=cursor.fetchall()
        for kul_parca in parcalar:
            self.urun_list.addItem(str(kul_parca[0]))
        
        font = QtGui.QFont()
        font.setPointSize(20)
        self.adet_label.setFont(font)
        self.adet_label.setObjectName("adet_label")
        self.adet_list = QtWidgets.QSpinBox(self.centralwidget)
        self.adet_list.setGeometry(QtCore.QRect(730, 300, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.adet_list.setFont(font)
        self.adet_list.setObjectName("adet_list")
        self.kullan_button = QtWidgets.QPushButton(self.centralwidget)
        self.kullan_button.setGeometry(QtCore.QRect(870, 290, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.kullan_button.setFont(font)
        self.kullan_button.setObjectName("kullan_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gunluk_label.setText(_translate("MainWindow", "G??nl??k Bak??m Plan??"))
        self.bakim_button.setText(_translate("MainWindow", "Bak??m Yap??ld??"))
        self.not_label.setText(_translate("MainWindow", "Not"))
        self.kullanilan_urun_label.setText(_translate("MainWindow", "Kullan??lan ??r??n"))
        self.adet_label.setText(_translate("MainWindow", "Adet"))
        self.kullan_button.setText(_translate("MainWindow", "KULLAN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
