# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt4demo1.ui'
#
# Created: Fri Apr 21 17:02:07 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import twitter_stream_download2 as tw2


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

class Ui_PaymentDlg(object):

	
    def SingleBrowse(self):
	#filePath = QtGui.QFileDialog.getOpenFileName(self,'Single File',"~/Desktop/",'*.txt')
	filePath = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/')
	#filePath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
	print("filePath: ",filePath, '\n')
	print ("Get file directory")
	self.lineEdit_6.setText(filePath)
		
    def functionRun(self):
    	print ("Clicked button Run")
    	import os
    	#os.system("python AAA/twitter_stream_download.py -q stream_PyQt_dust_2017_1 -d AAA/data")
	os.system("python AAA/twitter_stream_download.py -q stream_PyQt_dust_2017_2 -d AAA/data")

    def functionRun_Filter(self):
    	print ("Clicked button Run_Fiter")
    	import os
    	#os.system("python AAA/twitter_stream_download.py -q stream_PyQt_dust_2017_1 -d AAA/data")
	os.chdir("deep-learning-for-big-crisis-data-masterBinary")
	os.system("bash run_cnn.sh")
    	
    	

    def functionEnd(self,path):
    	print ("Clicked buton End")
    	subprocess.call(['python',path])
    	print("Name ",self.lineEdit.text())
    	print("Name ",self.lineEdit_2.text())
    	print("Name ",self.lineEdit_3.text())
    	#print("Name ",self.comboBox.())

    def runStreaming(self,  PaymentDlg):
    	tw2.run_Streaming()
    	

    def setupUi(self, PaymentDlg):
        PaymentDlg.setObjectName(_fromUtf8("PaymentDlg"))
        PaymentDlg.resize(420, 281)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("social.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PaymentDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(PaymentDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(PaymentDlg)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.splitter_4 = QtGui.QSplitter(self.tab)
        self.splitter_4.setGeometry(QtCore.QRect(9, 9, 380, 26))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.label_12 = QtGui.QLabel(self.splitter_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit = QtGui.QLineEdit(self.splitter_4)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.splitter_3 = QtGui.QSplitter(self.tab)
        self.splitter_3.setGeometry(QtCore.QRect(9, 41, 380, 25))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.label_13 = QtGui.QLabel(self.splitter_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_2 = QtGui.QLineEdit(self.splitter_3)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.splitter_2 = QtGui.QSplitter(self.tab)
        self.splitter_2.setGeometry(QtCore.QRect(9, 72, 380, 25))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.label_14 = QtGui.QLabel(self.splitter_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_3 = QtGui.QLineEdit(self.splitter_2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.splitter = QtGui.QSplitter(self.tab)
        self.splitter.setGeometry(QtCore.QRect(9, 103, 380, 25))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label_15 = QtGui.QLabel(self.splitter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.comboBox = QtGui.QComboBox(self.splitter)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.splitter_5 = QtGui.QSplitter(self.tab)
        self.splitter_5.setGeometry(QtCore.QRect(9, 134, 380, 25))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.label_16 = QtGui.QLabel(self.splitter_5)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.lineEdit_6 = QtGui.QLineEdit(self.splitter_5)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.pushButton_6 = QtGui.QPushButton(self.splitter_5)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 200, 178, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridlayout = QtGui.QGridLayout(self.tab_2)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setMargin(9)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridlayout.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(9, 9, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 0, 191, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 81, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 40, 191, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 81, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 190, 99, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(300, 0, 99, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(300, 40, 99, 27))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setEnabled(True)
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.pushButton = QtGui.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 121, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(self.tab_4)
        self.textEdit.setGeometry(QtCore.QRect(13, 40, 371, 78))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(PaymentDlg)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PaymentDlg)
        PaymentDlg.setTabOrder(self.lineEdit, self.lineEdit_2)
        PaymentDlg.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        PaymentDlg.setTabOrder(self.lineEdit_3, self.pushButton_2)
        PaymentDlg.setTabOrder(self.pushButton_2, self.pushButton_3)
        PaymentDlg.setTabOrder(self.pushButton_3, self.textEdit)
        PaymentDlg.setTabOrder(self.textEdit, self.pushButton)

    def retranslateUi(self, PaymentDlg):
        PaymentDlg.setWindowTitle(_translate("PaymentDlg", "Earthquake detection", None))
        self.label_12.setText(_translate("PaymentDlg", "Name file", None))
        self.label_13.setText(_translate("PaymentDlg", "Disaster", None))
        self.label_14.setText(_translate("PaymentDlg", "Keywords", None))
        self.label_15.setText(_translate("PaymentDlg", "Language", None))
        self.comboBox.setItemText(0, _translate("PaymentDlg", "English", None))
        self.comboBox.setItemText(1, _translate("PaymentDlg", "Korean", None))
        self.comboBox.setItemText(2, _translate("PaymentDlg", "Vietnamese", None))
        self.label_16.setText(_translate("PaymentDlg", "Store into", None))
        self.pushButton_6.setText(_translate("PaymentDlg", "Browser", None))
        self.pushButton_2.setText(_translate("PaymentDlg", "Run", None))
        self.pushButton_3.setText(_translate("PaymentDlg", "End", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PaymentDlg", "Collect", None))
        self.pushButton_4.setText(_translate("PaymentDlg", "Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PaymentDlg", "Pre-processing", None))
        self.label.setText(_translate("PaymentDlg", "CNN model", None))
        self.label_3.setText(_translate("PaymentDlg", "Input data", None))
        self.label_4.setText(_translate("PaymentDlg", "Results", None))
        self.pushButton_7.setText(_translate("PaymentDlg", "Run", None))
        self.pushButton_8.setText(_translate("PaymentDlg", "Browser", None))
        self.pushButton_9.setText(_translate("PaymentDlg", "Browser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("PaymentDlg", "Filtering", None))
        self.pushButton.setText(_translate("PaymentDlg", "Event detection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("PaymentDlg", "Detection", None))
        self.pushButton_6.clicked.connect(self.SingleBrowse)
        self.pushButton_3.clicked.connect(lambda:self.functionEnd('external.py'))
        self.pushButton_2.clicked.connect(self.functionRun)
        #self.connect(self.pushButton_3, SIGNAL("clicked()"),self.functionEnd)
        self.pushButton_8.clicked.connect(self.SingleBrowse)
        self.pushButton_9.clicked.connect(self.SingleBrowse)
        self.pushButton_7.clicked.connect(self.functionRun_Filter)
	self.pushButton.clicked.connect(self.runStreaming)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PaymentDlg = QtGui.QDialog()
    ui = Ui_PaymentDlg()
    ui.setupUi(PaymentDlg)
    PaymentDlg.show()
    sys.exit(app.exec_())

