# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stream_demo3.ui'
#
# Created: Thu May 11 17:55:15 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#import twitter_stream_download2 as tw2

import  ve2
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

#    def runStreaming(self):
 #   	
#	#self.Window = MyListener(self)
 #       #self.setWindowTitle("UIWindow")
 #       #self.setCentralWidget(self.Window)
 #       #self.Window.ToolsBTN.clicked.connect(self.startUIToolTab)
#        #self.show()
#	tw2.run_Streaming()
    def trainingCNN(self):
    	print ("Clicked button Run Training CNN model")
	print ("TRAINING.............................")
    	import os
    	os.system("bash run_cnn.sh")
    	
    def trainingRNN(self):
    	print ("Clicked button Run Training LSTM model")
	print ("TRAINING.............................")
    	import os
    	os.system("python rnn/lstm-anomaly-detection.py")
    	
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setAnimated(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
	
	icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./resource/social.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
	self.win_draw = ve2.MyWindow()
	#self.win_draw
	self.lang='english'

	
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 450, 85, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 450, 85, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 741, 128))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter_4 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label_12 = QtGui.QLabel(self.splitter_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit = QtGui.QLineEdit(self.splitter_4)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.splitter_4)
        self.splitter_3 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_13 = QtGui.QLabel(self.splitter_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_2 = QtGui.QLineEdit(self.splitter_3)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.splitter_2 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_14 = QtGui.QLabel(self.splitter_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))

        self.lineEdit_3 = QtGui.QLineEdit(self.splitter_2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.verticalLayout_2.addWidget(self.splitter_2)
        self.splitter = QtGui.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_15 = QtGui.QLabel(self.splitter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.comboBox = QtGui.QComboBox(self.splitter)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self._2 = QtGui.QGridLayout(self.tab_2)
        self._2.setSpacing(6)
        self._2.setMargin(9)
        self._2.setObjectName(_fromUtf8("_2"))

        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self._2.addWidget(self.pushButton_4, 2, 1, 1, 1)

	self.photo1 = QtGui.QPixmap("./resource/photo1.png")
        self.label_photo1 = QtGui.QLabel(self)
        self.label_photo1.setPixmap(self.photo1)
        self._2.addWidget(self.label_photo1)
	

        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
	#THEM
	#self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self._3 = QtGui.QGridLayout(self.tab_3)
        self._3.setSpacing(6)
        self._3.setMargin(9)
        self._3.setObjectName(_fromUtf8("_3"))

	#TAB3
 	self.pushButton_33 = QtGui.QPushButton(self.tab_3)
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self._3.addWidget(self.pushButton_33, 2, 1, 1, 1)
	self.photo2 = QtGui.QPixmap("./resource/photo2.png")
        self.label_photo2 = QtGui.QLabel(self)
        self.label_photo2.setPixmap(self.photo2)
        self._3.addWidget(self.label_photo2)

        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setEnabled(True)
        self.tab_4.setObjectName(_fromUtf8("tab_4"))

        self.pushButton = QtGui.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 121, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

	self.pushButton_ = QtGui.QPushButton(self.tab_4)
        self.pushButton_.setGeometry(QtCore.QRect(200, 10, 121, 27))
        self.pushButton_.setObjectName(_fromUtf8("pushButton_"))


	self.pushButton__ = QtGui.QPushButton(self.tab_4)
        self.pushButton__.setGeometry(QtCore.QRect(400, 10, 121, 27))
        self.pushButton__.setObjectName(_fromUtf8("pushButton__"))

	self.pushButton_Demo = QtGui.QPushButton(self.tab_4)
        self.pushButton_Demo.setGeometry(QtCore.QRect(600, 10, 121, 27))
        self.pushButton_Demo.setObjectName(_fromUtf8("pushButton_Demo"))

        self.listWidget = QtGui.QListWidget(self.tab_4)
        self.listWidget.setGeometry(QtCore.QRect(30, 60, 351, 421))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(self.tab_4)
        self.listWidget_2.setGeometry(QtCore.QRect(400, 60, 351, 421))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuEartquake = QtGui.QMenu(self.menubar)
        self.menuEartquake.setObjectName(_fromUtf8("menuEartquake"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionReal_application = QtGui.QAction(MainWindow)
        self.actionReal_application.setObjectName(_fromUtf8("actionReal_application"))
        self.actionTraining_phase = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../social.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTraining_phase.setIcon(icon)
        self.actionTraining_phase.setObjectName(_fromUtf8("actionTraining_phase"))
        self.menuEartquake.addAction(self.actionReal_application)
        self.menuEartquake.addAction(self.actionTraining_phase)
        self.menubar.addAction(self.menuEartquake.menuAction())


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "Run", None))
        self.pushButton_3.setText(_translate("MainWindow", "End", None))
        self.label_12.setText(_translate("MainWindow", "Name file", None))
        self.label_13.setText(_translate("MainWindow", "KeyWords", None))
        self.label_14.setText(_translate("MainWindow", "Limit Scope", None))
        self.label_15.setText(_translate("MainWindow", "Language", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "English", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Korean", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Vietnamese", None))
	self.comboBox.currentIndexChanged.connect(self.selectionchange)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Setting", None))
        self.pushButton_4.setText(_translate("MainWindow", "Training CNN model", None))
	self.pushButton_4.clicked.connect(self.trainingCNN)

	self.pushButton_33.setText(_translate("MainWindow", "Training Lstm model", None))
	self.pushButton_33.clicked.connect(self.trainingRNN)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Training CNN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Training RNN", None))

        self.pushButton.setText(_translate("MainWindow", "startStream", None))
	self.pushButton_.setText(_translate("MainWindow", "stopStream", None))
	self.pushButton__.setText(_translate("MainWindow", "GraphView", None))
	self.pushButton_Demo.setText(_translate("MainWindow", "Demo", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Detection", None))
        self.menuEartquake.setTitle(_translate("MainWindow", "Eartquake", None))
        self.actionReal_application.setText(_translate("MainWindow", "Real-application", None))
        self.actionTraining_phase.setText(_translate("MainWindow", "Training", None))
	self.pushButton_2.clicked.connect(self.getSetting)
	#self.listWidget.itemActivated.connect(self.printItemText)
	#self.listWidget_2.itemActivated.connect(self.printItemText)
	#self.listWidget.itemClicked.connect(self.Clicked)

    def printItemText(self):
        """These two are equivalent"""
        print("DIEMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",item.text())
        #print(self.listWidget.currentItem().text())

    def selectionchange(self,i):
      	print "Available language :"
		
      	for count in range(self.comboBox.count()):
        	print self.comboBox.itemText(count)
      	print "Current index",i,"selection changed ",self.comboBox.currentText()
	self.lang=str(self.comboBox.currentText()).lower()

    def getSetting(self):
        key= str(self.lineEdit_2.text())
	limit= str(self.lineEdit_3.text())
	#lang=self.comboBox.currentIndex()
        print("Keyword:",key)
	print("Limit:",limit)
	
	print("lang:",self.lang)
        key=key.split(",")
	limit=limit.split(",")
	print(key)
	print(type(limit))
	return key, limit

    def Clicked(self,item):
	QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())
#if __name__ == "__main__":
#    import sys
#    app = QtGui.QApplication(sys.argv)
#    MainWindow = QtGui.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#   MainWindow.show()
#    sys.exit(app.exec_())

