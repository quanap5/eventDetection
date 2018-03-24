#!/usr/bin/env python
#===================================================================================
#
#Editor: Nguyen Van Quan
#Date edit: 2017 May 15
#====================================================================================


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
from rnn import load_modelRNN_demo as lr
import ve2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
from numpy import *
from keras.preprocessing import sequence
import matplotlib.pyplot as plt

model=lm.load_model()
#modelRNN=lr.load_modelRNN()
#model2=lm.load_model()
#x=[[3, 3 ,3,3 ,3 ,3 ,3 ,3 ,3]]
#x = np.array(x)
#a=lr.load_modelRNN()
#print ("ANSERRRRRRRRR", lr.RNN_predict(modelRNN,x)[0,0])

keywords=['']
limits=['']
lang=['english']   


print ("##############################################################################")
print ("#########       ####           ############       ###                 ########")
print ("########  ##############  #################  ####  #######   #################")
print ("########   #############  #########    ####  ####  #######   #################")
print ("#########       ########  ########  #  ####  ###  ########   #################")
print ("###############  #######  #######      ####      #########   #################")
print ("###############  #######  ######  ###  ####  ###  ########   #################")
print ("########        ########  #####  ####  ####  ####  #######   #################")
print ("##################################################  ##########################")
initime=time.time()
#plt.ion()
check=0
import random

import re, os
import string 
import sys
import twokenize
import csv
from collections import defaultdict
from os.path import basename
import ntpath
import codecs
import unicodedata
def calctime(a):
    return time.time()-a
##########################################DEMO#########################################################################################################

class mythread_Demo(QtCore.QThread):
    
    #total = QtCore.pyqtSignal(object)
    #update = QtCore.pyqtSignal()
   
    def __init__(self,  listWidget, listWidget_2, win_draw):
        QtCore.QThread.__init__(self)
        #super(mythread, self).__init__(parent)
	#self.setupUi(self)
	self.listWidget=listWidget
	self.listWidget_2=listWidget_2
	self.win_draw=win_draw

    def addnew_Item_listWidget(self, in_text=''):
	
        if (self.listWidget.count() == 20):
		self.listWidget.clear()
        self.listWidget.addItem(in_text)
        	
    def addnew_Item_listWidget_2(self, in_text=''):
	if (self.listWidget_2.count() == 20):
		self.listWidget_2.clear()
	self.listWidget_2.addItem(in_text)

    def deleteItem(itemName):
	items_list = dialog.listWidget.findItems(itemName,QtCore.Qt.MatchExactly)
     	for item in items_list:
		r = dialog.listWidget.row(item)
		dialog.listWidget.takeItem(r)

	
    def run(self):
	global keywords, limits, lang
	#print(check_limit("i love uou", limits))
	tweet_count = 0
	file_in='demoEarthquake2016Sep12_Korea.json'
	#file_in='stream_earthquake5.json'
	#keyword_list=['quanap5']
	print("RUN DEMO:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::RUN DEMO")
        f= open(file_in, 'r')
	line = f.readline()
	while line and self.win_draw.check_stopDemo==0:
	    if 'created_at' in line and '"lang":"en"' in line and (check_limit(line.lower(),limits)): #('korea' in line.lower() or 'kor' in line.lower()) :
			#t=int(calctime(initime))
		        #f.write(data)
		       	#print(data)
			tweet_count += 1
			print ("AlREADY read: ", tweet_count ) 
 			all_data=json.loads(line)
        		tweet=all_data["text"].encode("utf-8")
			created_at=all_data['created_at'].encode("utf-8") 
  			timestamp_ms=all_data['timestamp_ms'].encode("utf-8") 		
        		#username=all_data["user"]["screen_name"]
        		#tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
			tweet=pre_process(tweet)
			
			print("TEXT:::", tweet)
			X_newinput  = lm.load_X_newinput(tweet)
			#Y_pred='0'
			Y_pred=str(model.predict_classes(X_newinput)[0][0])
			#Y_pred2=str(model2.predict_classes(X_newinput)[0][0])
			#print(X_newinput)
			print("ANSWER IS: ", Y_pred)
			#self.listWidget.addItem(tweet)
			#myQCustomQWidget = QCustomQWidget()
			#myQCustomQWidget.setIcon('earthquake.png')
			#self.delegate = ItemDelegate()
			username=all_data["user"]["screen_name"]
			self.win_draw.pushButtonPlot.setText(username)
			#self.win_draw.matplotlibWidget.axis.clear()
			#self.win_draw.matplotlibWidget.axis.plot(random.sample(range(0, 20),10))
			#xx=[[0, 0 ,0,0 ,0 ,0 ,0 ,0 ,0]]
    			#xx = np.array(xx)
			#modelRNN=lr.load_modelRNN()
			#print ("RNN_LSTM ANSWER", lr.RNN_predict(modelRNN,xx)[0,0])
 			#self.win_draw.matplotlibWidget.canvas.draw()
			#self.win_draw.on_pushButtonPlot_clicked(5,10)
			
			if Y_pred=='0':
				#self.listWidget.addItem(created_at + ": "+tweet)
				self.listWidget.scrollToBottom()
				self.win_draw.Accumulate(timestamp_ms)
				self.addnew_Item_listWidget(created_at + ": "+tweet)
				#self.win_draw.RealtimePlot()
			else:
				#self.listWidget_2.addItem(created_at + ": "+tweet)
				self.listWidget_2.scrollToBottom()
				#self.win_draw.Accumulate(timestamp_ms)
				self.addnew_Item_listWidget_2(created_at + ": "+tweet)
				#self.win_draw.RealtimePlot()
				#plt.axis([ 0, 70, -20,20])
        			#plt.xlabel('Time')
        			#plt.ylabel('Sentiment')
        			#plt.plot([t],20,'go',[t] ,30,'ro')
        			#plt.show()
	    line = f.readline()
	f.close()
	print ("# Tweets Imported:", tweet_count  )
  

    
#######################################################################################################################################################

class mythread(StreamListener, QtCore.QThread):
    
    #total = QtCore.pyqtSignal(object)
    #update = QtCore.pyqtSignal()
    
    def __init__(self,  listWidget, listWidget_2, win_draw):
	QtCore.QThread.__init__(self)
        #super(mythread, self).__init__(parent)
	#self.setupUi(self)
	self.listWidget=listWidget
	self.listWidget_2=listWidget_2
	self.win_draw=win_draw



    def addnew_Item_listWidget(self, in_text=''):
	
        if (self.listWidget.count() == 100):
		self.listWidget.clear()
        self.listWidget.addItem(in_text)
        	
    def addnew_Item_listWidget_2(self, in_text=''):
	if (self.listWidget_2.count() == 100):
		self.listWidget_2.clear()
	self.listWidget_2.addItem(in_text)


    def deleteItem(itemName):
	items_list = dialog.listWidget.findItems(itemName,QtCore.Qt.MatchExactly)
     	for item in items_list:
		r = dialog.listWidget.row(item)
		dialog.listWidget.takeItem(r)


    def on_data(self, data):
	global keywords, limits, lang
	
	try:
	    with open("streamming_quan.json", 'a') as f:
		if 'created_at' in data and '"lang":"en"' in data and (check_limit(data.lower(),limits)): #('' in data.lower() or '' in data.lower()) :
			t=int(calctime(initime))
		        #f.write(data)
		        #print(data)
 			all_data=json.loads(data)
        		tweet1=all_data["text"].encode("utf-8")
			created_at=all_data['created_at'].encode("utf-8") 
  			timestamp_ms=all_data['timestamp_ms'].encode("utf-8") 		
        		#username=all_data["user"]["screen_name"]
        		#tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
			tweet=pre_process(tweet1)
			print("TEXT:::", tweet)
			X_newinput  = lm.load_X_newinput(tweet)
			#Y_pred='0'
			Y_pred=str(model.predict_classes(X_newinput)[0][0])
			#Y_pred2=str(model2.predict_classes(X_newinput)[0][0])
			#print(X_newinput)
			print("ANSWER IS: ", Y_pred)
			#self.listWidget.addItem(tweet)
			#myQCustomQWidget = QCustomQWidget()
			#myQCustomQWidget.setIcon('earthquake.png')
			#self.delegate = ItemDelegate()
			username=all_data["user"]["screen_name"]
			self.win_draw.pushButtonPlot.setText(username)
			#self.win_draw.matplotlibWidget.axis.clear()
			#self.win_draw.matplotlibWidget.axis.plot(random.sample(range(0, 20),10))
			#x=[[3, 3 ,3,3 ,3 ,3 ,3 ,3 ,3]]
    			#x = np.array(x)
			#modelRNN=lr.load_modelRNN()
			#print ("ANSERRRRRRRRR", lr.RNN_predict(modelRNN,x)[0,0])
 			#self.win_draw.matplotlibWidget.canvas.draw()
			#self.win_draw.on_pushButtonPlot_clicked(5,10)
			
			if Y_pred=='0':
				#self.listWidget.addItem(created_at + ": "+tweet)
				
				self.win_draw.Accumulate(timestamp_ms)
				self.addnew_Item_listWidget(created_at + ": "+tweet)
				self.listWidget.scrollToBottom()
				#self.win_draw.RealtimePlot()
			else:
				#self.listWidget_2.addItem(created_at + ": "+tweet)
				
				self.addnew_Item_listWidget_2(created_at + ": "+tweet)
				self.listWidget_2.scrollToBottom()
				#self.win_draw.Accumulate(timestamp_ms)
				#self.win_draw.RealtimePlot()
			#plt.axis([ 0, 70, -20,20])
        		#plt.xlabel('Time')
        		#plt.ylabel('Sentiment')
        		#plt.plot([t],20,'go',[t] ,30,'ro')
        		#plt.show()


			
		        return tweet #True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True    
    def stop(self):
        self.runs = False

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
	global keywords, limits, lang
	#print (check_limit('i love you',limits))
	#self.getSetting()
        auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    	auth.set_access_token(config.access_token, config.access_secret)
    	api = tweepy.API(auth)
    	twitter_stream = Stream(auth,  mythread(self.listWidget ,self.listWidget_2, self.win_draw) )
    	#twitter_stream.filter(track=['earthquake','quake','flood'])
	twitter_stream.filter(track=keywords)
	print ("You should restart Earthquake detection demo")


 
# create the dialog for zoom to point

class progress(QtGui.QMainWindow,st.Ui_MainWindow):

    def __init__(self, parent=None): 
        super(progress, self).__init__(parent)
	self.setupUi(self)
        # Set up the user interface from Designer. 
        #self.setValue(0)
        self.pushButton.clicked.connect(self.startStream)
	self.pushButton_.clicked.connect(self.stopStream)
	self.pushButton__.clicked.connect(self.open_draw)
	self.pushButton_Demo.clicked.connect(self.startDemo)
	self.pushButton_.setEnabled(False)
        #self.thread = mythread(self.listWidget ,self.listWidget_2)
	#self.pushButton_.setEnabled(False)
	#Srun(self, self.thread)
       # self.thread.total.connect(self.setMaximum)
       # self.thread.update.connect(self.update)
        #self.thread.finished.connect(self.close)
        #self.thread = run(self)
        #self.n = 0
	#self.pushButtonPlot.setText("xxxxxx")
	#self.win_draw.show()
	self.win_draw.pushButtonPlot.setText("Quan Quan")
	#self.thread = mythread(self.listWidget ,self.listWidget_2,self.win_draw)
	#self.runs = True
	self.win_draw.check_stopDemo=0

    def getSettingX(self):
        key= str(self.lineEdit_2.text())
	limit= str(self.lineEdit_3.text())
	lang=str(self.lang)
	key=key.split(",")
	limit=limit.split(",")
        print("keyword",key)
	print("limit",limit)
	print("lang",lang)
        
	return key, limit ,lang
 
    def startStream(self):
	global keywords, limits,lang 
        keywords, limits,lang=self.getSettingX()
	self.thread = mythread(self.listWidget ,self.listWidget_2,self.win_draw)
	self.pushButton_.setEnabled(False)
	self.thread.start()
	self.pushButton.setEnabled(False)
	self.pushButton_.setEnabled(True)
	self.pushButton_Demo.setEnabled(False)
	self.win_draw.check_stopDemo=1
	
    def startDemo(self):
	global keywords, limits,lang 
	keywords, limits,lang=self.getSettingX()
	print ('DEMO DEMO DEMO DEMO')
	self.mythread_Demo = mythread_Demo(self.listWidget ,self.listWidget_2,self.win_draw)
	self.pushButton_Demo.setEnabled(False)
	self.mythread_Demo.start()
	self.pushButton.setEnabled(False)
	self.pushButton_.setEnabled(True)
	self.win_draw.check_stopDemo=0


    def stopStream(self):
	
	if self.win_draw.check_stopDemo==0:
		self.win_draw.check_stopDemo=1
		self.pushButton.setEnabled(True)
		self.pushButton_.setEnabled(False)
		self.pushButton_Demo.setEnabled(True)
		self.mythread_Demo.terminate()
	else:
		#self.thread.stop()
        	#self.thread.wait()
		self.thread.terminate()
		self.pushButton.setEnabled(True)
		self.pushButton_.setEnabled(False)
		self.pushButton_Demo.setEnabled(True)
		print ('stop streamming')
		QtGui.QMessageBox.information(self, "", "Stop Streaming")

    def runStream(self):
	self.listWidget.addItem("-----------------------------------------------------------")
	self.listWidget_2.addItem("----------------------------------------------------------")
    def open_draw(self):
	global check
 	if check % 2==1:
		self.win_draw.hide()
		self.pushButton__.setText("GraphView")
		check =check+1
	else:
		#self.win_draw.resize(666, 333)
    		self.win_draw.show()
		self.pushButton__.setText("Close Graph")
		check=check-1
def check_limit2(line, limits):
	check=0
	for i in range(0,len(limits)):
		#print (i)
		if limits[i] in line.lower():
			#print (limits[i])
			check=check+1
	#print (check)
	if check>0 :
		return True
	else:
		return False
	
def check_limit(b, a):
    return any([i in b for i in a])


def pre_process(tweet):

#	print "[original]", tweet
	#print(tweet)
	# 0. Removing special Characters
	#punc = '$%^&*()_+-={}[]:"|\'\~`<>/,'
	#trans = string.maketrans(punc, ' '*len(punc))
	#tweet = tweet.translate(trans)
	# 1. Normalizing utf8 formatting
	tweet = tweet.decode("unicode-escape").encode("utf8").decode("utf8")
	#tweet = tweet.encode("utf-8")
	tweet = tweet.encode("ascii","ignore")
	tweet = tweet.strip(' \t\n\r')

	# 1. Lowercasing
	tweet = tweet.lower()
#	print "[lowercase]", tweet

	# Word-Level
	tweet = re.sub(' +',' ',tweet) # replace multiple spaces with a single space

	# 2. Normalizing digits
	tweet_words = tweet.strip('\r').split(' ')
	for word in [word for word in tweet_words if word.isdigit()]:
		tweet = tweet.replace(word, "D" * len(word))
#	print "[digits]", tweet

	# 3. Normalizing URLs
	tweet_words = tweet.strip('\r').split(' ')
	for word in [word for word in tweet_words if '/' in word or '.' in word and  len(word) > 3]:
		tweet = tweet.replace(word, "httpAddress")
#	print "[URLs]", tweet

	# 4. Normalizing username
	tweet_words = tweet.strip('\r').split(' ')
	for word in [word for word in tweet_words if word[0] == '@' and len(word) > 1]:
		tweet = tweet.replace(word, "usrId")
#	print "[usrename]", tweet

	# 5. Removing special Characters
	punc = '@$%^&*()_+-={}[]:"|\'\~`<>/,'
	trans = string.maketrans(punc, ' '*len(punc))
	tweet = tweet.translate(trans)
#	print "[punc]", tweet

	# 6. Normalizing +2 elongated char
	tweet = re.sub(r"(.)\1\1+",r'\1\1', tweet.decode('utf-8'))
#	print "[elong]", tweet

	# 7. tokenization using tweetNLP
	tweet = ' '.join(twokenize.simpleTokenize(tweet))
#	print "[token]", tweet 

	#8. fix \n char
	tweet = tweet.replace('\n', ' ')

	#prccd_item_list.append(tweet.strip())
#	print "[processed]", tweet.replace('\n', ' ')
	return tweet
def main():
    app = QtGui.QApplication([])
    #win_draw = ve2.MyWindow()
    progressWidget = progress()
    progressWidget.move(300, 300)
    progressWidget.show()
    #win_draw.resize(800, 600)
    #win_draw.show()
    app.exec_()

if __name__ == '__main__':
    main()
