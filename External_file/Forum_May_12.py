import tweepy
from PyQt4 import QtCore, QtGui
import sys, time
import stream_demo3 as st 
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import config
import json
import re
import threading
import load_model_demo as lm
from keras.preprocessing import sequence


model=lm.load_model()
class mythread(StreamListener, QtCore.QThread):
    
    #total = QtCore.pyqtSignal(object)
    #update = QtCore.pyqtSignal()
    
    def __init__(self,  listWidget, listWidget_2):
        QtCore.QThread.__init__(self)
        #super(mythread, self).__init__(parent)
	#self.setupUi(self)
	self.listWidget=listWidget
	self.listWidget_2=listWidget_2

    def on_data(self, data):
	#global model
        try:
            with open("streamming_quan.json", 'a') as f:

		        f.write(data)
		        #print(data)
 			all_data=json.loads(data)
        		tweet=all_data["text"].encode("utf-8")
        		#username=all_data["user"]["screen_name"]
        		tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
			print("TEXT:::", tweet)
			X_newinput  = lm.load_X_newinput(tweet)
			Y_pred=str(model.predict_classes(X_newinput)[0][0])
			print(X_newinput)
			print("ANSWER IS: ", Y_pred)
			#self.listWidget.addItem(tweet)
			if Y_pred=='0':
				self.listWidget.addItem(tweet)
			else:
				self.listWidget_2.addItem(tweet)
		        return tweet #True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True    
 
    def run_t(self):
        #self.total.emit(self.n)
        i = 0
	while True:
                print ("Nguyen van Quan ", str(i))
		
                i=i+1
		if i%2==0:
			self.listWidget.addItem("NGUYEN VAN QUAN")
		else:
			self.listWidget_2.addItem("TRAC THI THUY")
		time.sleep(5)
    def run(self):
    #while True:
        auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    	auth.set_access_token(config.access_token, config.access_secret)
    	api = tweepy.API(auth)
    	twitter_stream = Stream(auth,  mythread(self.listWidget ,self.listWidget_2) )
    	twitter_stream.filter(track=['earthquake'])
	print ("quan co len quan oi")
 
# create the dialog for zoom to point
class progress(QtGui.QMainWindow,st.Ui_MainWindow):
    
    def __init__(self, parent=None): 
        super(progress, self).__init__(parent)
	self.setupUi(self)
        # Set up the user interface from Designer. 
        #self.setValue(0)
        self.pushButton.clicked.connect(self.runStream)
        self.thread = mythread(self.listWidget ,self.listWidget_2)
	#Srun(self, self.thread)
       # self.thread.total.connect(self.setMaximum)
       # self.thread.update.connect(self.update)
        #self.thread.finished.connect(self.close)
        #self.thread = run(self)
        #self.n = 0
        self.thread.start()
        
    #def update(self):
    #    self.n += 1
    #    print self.n
        #self.setValue(self.n)
    def runStream(self):
	self.listWidget.addItem("-----------------------------------------------------------")
	self.listWidget_2.addItem("----------------------------------------------------------")
 
def main():
    app = QtGui.QApplication([])
    progressWidget = progress()
    progressWidget.move(300, 300)
    progressWidget.show()
    app.exec_()

if __name__ == '__main__':
    main()
