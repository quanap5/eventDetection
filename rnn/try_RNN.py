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
import ve
import numpy as np
from keras.preprocessing import sequence
import matplotlib.pyplot as plt
a=lr.load_modelRNN()

	x=[[3, 3 ,3,3 ,3 ,3 ,3 ,3 ,3]]
	x = np.array(x)
	#a=lr.load_modelRNN()
	print ("ANSERRRRRRRRR", lr.RNN_predict(a,x)[0,0])
