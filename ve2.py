#!/usr/bin/env python
#-*- coding:utf-8 -*-
from __future__ import print_function
import random

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PyQt4 import QtGui, QtCore
import matplotlib.pyplot as plt
import time
import random
import pylab
from pylab import *
from utilities2 import aidr2
from rnn import load_modelRNN_demo as lr
import numpy as np
from scipy.stats import norm

len_val=800
len_his=180
values=[]
values = [0 for x in range(len_val)]

predicted_values=[]
predicted_values = [0 for x in range(len_val+1)]

earth_candidate=[]
earth_candidate = [-10 for x in range(len_val)]

earth_detect=[]
earth_detect = [-10 for x in range(len_val)]

max_freq=5

t0=0;
inter_count=0;
m_count=1;
interval_='20' #interval to accumulated, 10 seconds
Acc_Tweets=0;
#timeSeries

modelRNN=lr.load_modelRNN()
x=[[3, 3 ,3,3 ,3 ,3 ,3 ,3 ,3]]
x = np.array(x)
print ("ANSERRRRRRRRR", lr.RNN_predict(modelRNN,x)[0,0])

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MatplotlibWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.axis = self.figure.add_subplot(111)

        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.canvas)

	# set the limit for the x and y
	xAchse=pylab.arange(0,len_val,1)
	yAchse=pylab.array([0]*len_val)
        self.axis.set_xlim(0., len_val+50)
        self.axis.set_ylim(-1.5,10)	
	self.axis.grid(True)
	self.axis.set_title("Realtime Frequency Plot")
	self.axis.set_xlabel("Time")
	self.axis.set_ylabel("Frequency")
	#self.axis([0,100,-1.5,1.5])
	self.axis.plot(xAchse,yAchse,'-')
	
	

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.resize(800, 600)
	self.setWindowTitle("Real-time Graph View")
        self.pushButtonPlot = QtGui.QPushButton(self)
        self.pushButtonPlot.setText("Plot")
        self.pushButtonPlot.clicked.connect(self.on_pushButtonPlot_clicked)

        self.matplotlibWidget = MatplotlibWidget(self)
        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.pushButtonPlot)
        self.layoutVertical.addWidget(self.matplotlibWidget)
	#self.modelRNN=lr.load_modelRNN()
	self.line1,self.line2,self.line3, self.line4=self.matplotlibWidget.axis.plot(values[-len_val:],'g-', predicted_values[-len_val-1:],'r-',earth_candidate[-len_val:],'yo',earth_detect[-len_val:],'r*')
	#self.line3=self.matplotlibWidget.axis.plot()

	self.listWidget_ve = QtGui.QListWidget(self)
        self.listWidget_ve.setGeometry(QtCore.QRect(400, 60, 351, 421))
        self.listWidget_ve.setObjectName(_fromUtf8("listWidget_ve"))
	self.layoutVertical.addWidget(self.listWidget_ve)
               
      
    def on_pushButtonPlot_clicked(self):
        print("You have just clicked to see the lastest 10 frequency")
	#self.matplotlibWidget.canvas.draw()
	self.pushButtonPlot.setText(str(values[-9:]))

  
    def RealtimePlot(self):
	global values
	#self.matplotlibWidget.axis.clear()
	#timeSeries=self.matplotlibWidget.axis.plot(values[-100:])
	#self.matplotlibWidget.axis.lines.remove(timeSeries[0])
	self.line1,self.line2,self.line3, self.line4=self.matplotlibWidget.axis.plot(values[-len_val:],'g-', predicted_values[-len_val-1:],'r-',earth_candidate[-len_val:],'yo',earth_detect[-len_val:],'r*')
	self.matplotlibWidget.canvas.draw()

    def Accumulate(self, timestamp_ms):
	global values, t0 ,inter_count, m_count, interval_, Acc_Tweets, max_freq
	timestamp_ms=long(timestamp_ms)
	#self.matplotlibWidget.axis.lines.pop(0)
	if t0==0:
		t0=timestamp_ms
		inter_count=0
	if timestamp_ms<=t0+float(interval_)*1000:
		inter_count+=1
	else:
		#csv_time1.writerow([t0,time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(t0/1000.)), inter_count])
		values.append(inter_count)
		mse_new=values[-1]-predicted_values[-1]
		mse = abs(np.array(values[-len_his:]) - np.array(predicted_values[-len_his:]))
		#mse = abs(np.array(values[:]) - np.array(predicted_values[:]))
		mu, std = norm.fit(mse)
		if (norm.pdf(mse_new, mu, std) <0.0001) :
			earth_candidate.append(-1)
			
			#self.listWidget_ve.addItem(str(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(t0/1000.))) + ": candidate"+ str(values[-1]))
			#self.listWidget_ve.scrollToBottom()
			
			#self.listWidget.addItem(created_at + ": "+tweet)
		else:
			earth_candidate.append(-10)

		if sum(earth_candidate[-4:])> -23.:
			self.listWidget_ve.addItem(str(time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(t0/1000.))) + ": EARTHQUAKE"+ str(values[-1]))
			#self.listWidget_ve.scrollToBottom()
			earth_detect.append(-0.5)
		else:
			earth_detect.append(-10)
			
		#self.matplotlibWidget.axis.lines.pop(0)
		self.matplotlibWidget.axis.lines.remove(self.line1)
		self.matplotlibWidget.axis.lines.remove(self.line2)
		self.matplotlibWidget.axis.lines.remove(self.line3)
		self.matplotlibWidget.axis.lines.remove(self.line4)

		self.RealtimePlot()
		pred=self.Auto_predict(max_freq, values[-9:])
		predicted_values.append(pred)
		print ("=========================================================================== ")
		print ("Time slot # 0:  ", time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(t0/1000.)))
		print ("=========================================================================== ")
		no_loop=0
		while (timestamp_ms > t0+float(interval_)*1000*(2+no_loop)):
			#csv_time1.writerow([t0+float(interval_)*1000*(2+no_loop-1),time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime((t0+float(interval_)*1000*(2+no_loop-1))/1000.)), 0])
			values.append(0)
			mse_new=values[-1]-predicted_values[-1]
			#mse = abs(np.array(values[-len_val:]) - np.array(predicted_values[-len_val:]))
			#mu, std = norm.fit(mse)
#			if norm.pdf(mse_new,  mu, 3*std) <0.0001:
				#earth_candidate.append(-10)
				#self.listWidget_ve.addItem("earthquake")
				#self.listWidget_ve.scrollToBottom()
#			else:
				#earth_candidate.append(-10)
			earth_candidate.append(-10)
			if sum(earth_candidate[-4:])> -23.:
				self.listWidget_ve.addItem(str(time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime((t0+float(interval_)*1000*(2+no_loop-1))/1000.))) + ": EARTHQUAKE"+ str(values[-1]))
				self.listWidget_ve.scrollToBottom()
				earth_detect.append(-0.5)
			else:
				earth_detect.append(-10)		
			#self.matplotlibWidget.axis.lines.pop(0)
			self.matplotlibWidget.axis.lines.remove(self.line1)
			self.matplotlibWidget.axis.lines.remove(self.line2)
			self.matplotlibWidget.axis.lines.remove(self.line3)
			self.matplotlibWidget.axis.lines.remove(self.line4)
			self.RealtimePlot()
			pred=self.Auto_predict(max_freq,values[-9:])
			predicted_values.append(pred)
			print ("=========================================================================== ")
			print ("Time slot: 0 tweet ", time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime((t0+float(interval_)*1000*(2+no_loop-1))/1000.)))
			print ("=========================================================================== ")
			no_loop+=1
		Acc_Tweets+=1
		inter_count=1
		#m_count+=1;
		t0=t0+float(interval_)*1000*(2+no_loop-1)
		print ("SIZE", str(len(values)), str(len(predicted_values)),str(len(earth_candidate)),str(len(earth_detect)))


    def Auto_predict(self,max_freq,sq_observation):
	global modelRNN
	sq_observation1 = map(lambda x: x/max_freq, sq_observation)
	array1=[]
        array1.append(sq_observation1)
	
        array1 = np.array(array1)	
	#x=[[1, 1 ,1,1 ,1 ,1 ,1 ,1 ,1]]
	#x = np.array(x)
	#a=lr.load_modelRNN()
	
	print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ")
	print ("XX                 RNN model                               XX ")
	print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ")
	#out= np.rint(max_freq*lr.RNN_predict(modelRNN,array1)[0,0])
	out=max_freq*lr.RNN_predict(modelRNN,array1)[0,0]
	print ("ANSERRRRRRRRR",sq_observation , "===> ",out)
	return out
		
if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.resize(666, 333)
    main.show()

    sys.exit(app.exec_())
