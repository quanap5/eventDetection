# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stream_demo.ui'
#
# Created: Thu May 11 00:52:04 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json
import re
from utilities2 import aidr2
import load_model_demo as lm
from keras.preprocessing import sequence


model=lm.load_model()
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, QWidget
#import twitter_stream_download2 as tw2
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



def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser


class Ui_PaymentDlg(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Ui_PaymentDlg, self).__init__()
	#self.setupUi(self)

    #def __init__(self, parent = None):
        #QtGui.QWidget.__init__(self, parent)
	#super(Ui_PaymentDlg, self).__init__(parent)
    def runStreaming(self):
    	
	#self.Window = MyListener(self)
        #self.setWindowTitle("UIWindow")
        #self.setCentralWidget(self.Window)
        #self.Window.ToolsBTN.clicked.connect(self.startUIToolTab)
        #self.show()
	run_Streaming()

    def setupUi(self, PaymentDlg):
        PaymentDlg.setObjectName(_fromUtf8("PaymentDlg"))
        PaymentDlg.resize(420, 281)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../social.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.listWidget = QtGui.QListWidget(self.tab_4)
        self.listWidget.setGeometry(QtCore.QRect(0, 60, 191, 141))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(self.tab_4)
        self.listWidget_2.setGeometry(QtCore.QRect(200, 60, 191, 141))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.listWidget.addItem("Nguyen Nguyen Nguyen")

        self.retranslateUi(PaymentDlg)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(PaymentDlg)
        PaymentDlg.setTabOrder(self.lineEdit, self.lineEdit_2)
        PaymentDlg.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        PaymentDlg.setTabOrder(self.lineEdit_3, self.pushButton_2)
        PaymentDlg.setTabOrder(self.pushButton_2, self.pushButton_3)
        PaymentDlg.setTabOrder(self.pushButton_3, self.pushButton)

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
	self.pushButton.clicked.connect(self.runStreaming)

class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    #def __init__(self, data_dir, query):
    #    query_fname = format_filename(query)
    #    self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)
    def __init__(self, parent = None):
    #    #QtGui.QWidget.__init__(self, parent)
	 super(MyListener, self).__init__(parent)
    #    #self.ui = Ui_PaymentDlg()
         #self.ui = Ui_PaymentDlg()
	 
        # self.ui.setupUi(self)
         #self.pushButton.clicked.connect(self.trythoi)
   # def trythoi(self):
     #   print ("Deo gi")
 

    def on_data(self, data):
	#global model
        try:
            with open("streamming_quan.json", 'a') as f:
		#if 'korea' in data:
		        f.write(data)
		        #print(data)
 			all_data=json.loads(data)
        		tweet=all_data["text"].encode("utf-8")
        		#username=all_data["user"]["screen_name"]
        		tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
			print("TEXT:::", tweet)
			#model=lm.load_model()
			#X_newinput=[[1, 40445, 55824, 52346, 67196, 72368, 76113, 49609, 45222, 77017, 18685, 43795, 44566, 20744, 18336, 71466, 16945, 42630, 23024, 56334, 58251, 53247, 67560]]
			#X_newinput  = sequence.pad_sequences(X_newinput,  100)
			X_newinput  = lm.load_X_newinput(tweet)
			print(X_newinput)
			print("ANSWER IS: ", model.predict_classes(X_newinput))
			#Sself.show()
            		self.listWidget.addItem("Quan Nguyen Van")
			


#			t0 = time.clock()
#			X_newinput= aidr2.load_and_numberize_data2(input_tweet,path=data_dir, nb_words=max_features, init_type=init_type, embfile=emb_file, validate_train_merge=0, #map_labels_to_five_class=0)
#			print ("Thoi gian map to vector ", time.clock() - t0)
#			print ( X_newinput) 
#			X_newinput  = sequence.pad_sequences(X_newinput,  maxlen)#Quan them vao--------------------
		        return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True


def format_filename(fname):
    """Convert file name into a safe string.

    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.

    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

def run_Streaming():
    
    parser = get_parser()
    args = parser.parse_args()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)


    

    #twitter_stream = Stream(auth, MyListener(args.data_dir, args.query))
    twitter_stream = Stream(auth, MyListener())
    #twitter_stream.filter(track=[args.query])
    twitter_stream.filter(track=['earthquake'])
#,'quake','terremoto','maremoto','gempa','tsunami','deprem','zelzele','lindol'])
    #twitter_stream.filter(locations=[124, 33, 130, 38])#GEO_KOREA
    #twitter_stream.filter(locations=[-180, -90, 180, 90])#GEO_WORLD



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PaymentDlg = QtGui.QDialog()
    ui = Ui_PaymentDlg()
    ui.setupUi(PaymentDlg)
    PaymentDlg.show()
    sys.exit(app.exec_())

