# Read me first: Tutorial
# Edit the config file where contain your keys
# Make a new folder for example: data
# Run code using command: python twitter_stream_download.py -q apple -d data
# Data will be stored under JSON format
##################################################################################################
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
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
import stream_demo3 as st
model=lm.load_model()
import sys
import threading
import time

class MyListener(StreamListener,QThread):
    """Custom StreamListener for streaming data."""

    #def __init__(self, data_dir, query):
    #    query_fname = format_filename(query)
    #    self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)
    def __init__(self):
        QThread.__init__(self)
       # self.setWindowTitle("Child Window!")
   	#self.data = data
	#thread = threading.Thread(target=self.run, args=())
        #thread.daemon = True                            # Daemonize thread
	#thread.start()
    def __del__(self):
        self.wait()

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
			#QtGui.QMessageBox.critical(self, "No subreddits", "You didn't enter any subreddits.", QtGui.QMessageBox.Ok)


#			t0 = time.clock()
#			X_newinput= aidr2.load_and_numberize_data2(input_tweet,path=data_dir, nb_words=max_features, init_type=init_type, embfile=emb_file, validate_train_merge=0, #map_labels_to_five_class=0)
#			print ("Thoi gian map to vector ", time.clock() - t0)
#			print ( X_newinput) 
#			X_newinput  = sequence.pad_sequences(X_newinput,  maxlen)#Quan them vao--------------------
		        return tweet #True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True

    def run(self):
	while True:
            auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    	    auth.set_access_token(config.access_token, config.access_secret)
    	    api = tweepy.API(auth)
    	    twitter_stream = Stream(auth, MyListener())
    	    twitter_stream.filter(track=['earthquake'])
	    print ("quan co len quan oi")
	#time.sleep(1)
    	#self.sleep(2)
    	#auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    	#auth.set_access_token(config.access_token, config.access_secret)
    	#api = tweepy.API(auth)
    	#twitter_stream = Stream(auth, MyListener())
    	#twitter_stream.filter(track=['earthquake'])


class ThreadingTutorial(QtGui.QMainWindow, st.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.start_getting_top_posts)
        self.pushButton.clicked.connect(self.runStream)
    def runStream(self):
	self.listWidget.addItem("LIST 2")
	self.listWidget_2.addItem("LIST 2")
        auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    	auth.set_access_token(config.access_token, config.access_secret)
    	api = tweepy.API(auth)
    	twitter_stream = Stream(auth, MyListener())
    	twitter_stream.filter(track=['earthquake','quake','shake'])
	#self.get_thread=getPostsThread(subreddit_list)
	#self.listWidget.addItem("LIST 2")
	#self.listWidget_2.addItem("LIST 2")


    def start_getting_top_posts(self):
	print ("Test thu xem")
	self.listWidget.addItem("LIST 2")
	self.listWidget_2.addItem("LIST 2")



def main():
    app = QtGui.QApplication(sys.argv)
    form = ThreadingTutorial()
    #example = MyListener()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
