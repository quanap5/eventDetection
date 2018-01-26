#!/usr/bin/env python
#===================================================================================
#This contain function that loads trained model and numerical transformation new data
#Editor: Nguyen Van Quan
#Date edit: 2017 April 24
#====================================================================================

from __future__ import print_function
import numpy as np
# fix random seed for repoducibility
seed=7# quan sua  1337-->7
np.random.seed(seed)  # for reproducibility

# keras related
from keras.models import Sequential
from keras.layers.core    import Dense, Dropout, Activation, Flatten
from keras.preprocessing import sequence
from keras.layers.embeddings import Embedding
from keras.layers.convolutional import Convolution1D, MaxPooling1D
from utilities2 import aidr2
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.utils import np_utils
from keras.models import model_from_json

#other utilities 
import optparse
import logging
import sys
import csv
import os, sys
import time
import datetime
csv.field_size_limit(sys.maxsize)



from sklearn import metrics

def main():
        CNN_SCR="./dnn_scripts/loadAndUsing.py"  #Load and Using
        MODEL_DIR="saved_modelsBinary/"

        data_dir="./data/nn_data/"
        log="./logBinary.cnn"

        #os.mkdir (MODEL_DIR, 0755)

        ###<- Set general DNN settings ->
        dr_ratios=(0.2) #dropout_ratio
        mb_sizes=(128)  #minibatch-size

        ### <- set CNN settings ->
        nb_filters=(150) #no of feature map
        filt_lengths=(2)
        pool_lengths=(3) 

        vocab_sizes=(90.0) # how many words in percentage for vocabulary

        ### <- embedding file ->
        init_type="pretrained"
        emb_file="./embeddings/glove_twitter_27B_200d.text"
        tweet_str="rt usrId rashid plz share widely rss diverted funds from uk meant for gujarat earthquake relief to fund shakha activities ! https"


        mapper(input_tweet =tweet_str
        ,log_file       = log
        ,data_dir       = data_dir
        ,data_spec      = "in"
        ,model_dir      = MODEL_DIR

        ,maxlen         = 100

        ,nb_filter      = nb_filters
        ,filter_length  = filt_lengths     
        ,pool_length    = pool_lengths
        ,max_features   = vocab_sizes
        ,emb_size       = 128
        ,hidden_size    = 128
        ,dropout_ratio  = dr_ratios

        ,init_type      = init_type
        ,emb_file       = emb_file
        ,tune_emb       = True

        ,learn_alg      = "adam" # sgd, adagrad, rmsprop, adadelta, adam (default)   #-----------------Quan sua  adadelta--> sgd
        ,minibatch_size = mb_sizes #-quan sua 32-->128
        ,loss           = "binary_crossentropy" # hinge, squared_hinge, binary_crossentropy (default)
        ,epochs         = 25)  #-quan sua 25-->100



def mapper(input_tweet
        ,log_file       = "log"
        ,data_dir       = "../data/earthquakes/in/"
        ,data_spec      = "in"
        ,model_dir      = "./saved_models/"

        ,maxlen         = 100

        ,nb_filter      = 250
        ,filter_length  = 3     
        ,pool_length    = 2
        ,max_features   = 80
        ,emb_size       = 128
        ,hidden_size    = 128
        ,dropout_ratio  = 0.0

        ,init_type      = 'random' 
        ,emb_file       = "../data/unlabeled_corpus.vec"
        ,tune_emb       = True

        ,learn_alg      = "adam" # sgd, adagrad, rmsprop, adadelta, adam (default)   #-----------------Quan sua  adadelta--> sgd
        ,minibatch_size = 128  #-quan sua 32-->128
        ,loss           = "binary_crossentropy" # hinge, squared_hinge, binary_crossentropy (default)
        ,epochs         = 25   #-quan sua 25-->100
    ):
    

        #print('Loading data...')
        print('LOADING DATA...')
        print('----------------------------------------------------------------')
        input_="rt usrId rashid plz share widely rss diverted funds from uk meant for gujarat earthquake relief to fund shakha activities ! https"
	t0 = time.clock()
        X_newinput= aidr2.load_and_numberize_data2(input_tweet,path=data_dir, nb_words=max_features, init_type=init_type, embfile=emb_file, validate_train_merge=0, map_labels_to_five_class=0)
	print ("Thoi gian map to vector ", time.clock() - t0)
	print ( X_newinput)
        X_newinput  = sequence.pad_sequences(X_newinput,  maxlen)#Quan them vao--------------------
            #print(X_train[0]) #quan them vao

        #build model...
    #   nb_classes = np.max(y_train) + 1
        nb_classes=2
        if nb_classes == 2: # binary
            loss       = loss
            #class_mode = "binary"
            optimizer  = learn_alg
    #
        elif nb_classes > 2: # multi-class
            loss       = 'categorical_crossentropy'
            #class_mode = 'categorical'
            optimizer  = learn_alg
            print("** optimizer: " + learn_alg) 
            # convert class vectors to binary class matrices [ 1 of K encoding]



    #######################LOAD MODEL ###########################################
	model_name = model_dir + "cnn" + "-" + optimizer + "-" + str(nb_filter) + "-" + str(filter_length) + \
"-" + str(pool_length) + "-" + str (tune_emb) +\
"-" + loss + "-" + str (minibatch_size) + "-" + str(dropout_ratio) + "-init-" + str (init_type) + "-" +\
str (max_features) + "-" + str (emb_size) + "-" + str (hidden_size) + ".model.cl." + str(nb_classes) + ".dom." + str(data_spec) 

	model = model_from_json(open(model_name + ".json").read())
	model.load_weights(model_name+".h5")
	model.compile(optimizer=optimizer, loss=loss, metrics=["accuracy"] )#,  class_mode=class_mode) #--Quan bo class_mode=calss_mosde va them metrics=["accuracy"]
        t1 = time.clock()

	y_newinput_pred = model.predict_classes(X_newinput,batch_size=1024)
	
	print ("Thoi gian tinh toan 1 tweet", time.clock() - t1)
        print("INPUT: "+ str(len(X_newinput)))
        print("INPUTlabelPred: "+ str(len(y_newinput_pred)))
        print("The last date and time EXECUTED: " , datetime.datetime.now())    

        with open("LabelPred.csv", "w") as t:
                writer = csv.writer(t)
                writer.writerows(y_newinput_pred)



#################################################################################
    
if __name__ == "__main__":
	main()




