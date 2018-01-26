#!/usr/bin/env python
#===================================================================================
#This contain function that loads trained model and numerical transformation new data
#Editor: Nguyen Van Quan
#Date edit: 2017 May 15
#====================================================================================


from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import time
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from numpy import arange, sin, pi, random
import csv
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import norm
from keras.models import model_from_json

np.random.seed(1234)

# Global hyper-parameters
sequence_length = 10
random_data_dup = 20  # each sample randomly duplicated between 0 and 9 times, see dropin function
epochs = 1
batch_size = 512#50
percent=0.5
max_freq=50

def load_modelRNN():
    t0 = time.clock()
    model_dir = "./saved_modelRNN/"
    json_file = open(model_dir+'modelLSTM.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.compile(loss='mean_squared_error', optimizer='adam')
    # load weights into new model
    loaded_model.load_weights(model_dir+"modelLSTM.h5")
    print("Loaded model from disk")
    #modelRNN=loaded_model
    #modelRNN.compile(loss="mse", optimizer="rmsprop")
    
    print('LOADING MODEL RNN.............///////////////////////////////////////...')
    print ("RNN model: Time cost to loadd model_RNN ", time.clock() - t0)
    return loaded_model

def RNN_predict(modelRNN,current_input):
    #global model
    current_input
    print("Shape X_predict", np.shape(current_input))
    X_pred = np.reshape(current_input, (current_input.shape[0], current_input.shape[1], 1))
    #current_input
    print("Shape X_predict2222222222", np.shape(X_pred))
    predicted = modelRNN.predict(X_pred)
    
    return  predicted




#load_modelRNN_andPredict()
#x=[[1, 1 ,1,1 ,1 ,1 ,1 ,1 ,1]]
#x = np.array(x)
#a=load_modelRNN()
#print ("ANSERRRRRRRRR", RNN_predict(a,x)[0,0])
