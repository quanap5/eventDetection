#===================================================================================
#This scrip file to read json file for Earthquake project
#Editor: Nguyen Van Quan
#Date edit: 2017 April 08
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
from utilities import aidr2
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.utils import np_utils
from keras.models import model_from_json

#other utilities 
import optparse
import logging
import sys
import csv
import os
import time
import datetime
csv.field_size_limit(sys.maxsize)



from sklearn import metrics



if __name__ == '__main__':

	
	logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

	# parse user input
	parser = optparse.OptionParser("%prog [options]")

	#parser.add_option("-Q", "--input-tweet",	dest="input_tweet",       type="str", help="this is input tweet")

	#file related options
	parser.add_option("-g", "--log-file",          dest="log_file", help="log file [default: %default]")
	parser.add_option("-d", "--data-dir",          dest="data_dir", help="directory containing train, test and validate file [default: %default]")
	parser.add_option("-D", "--data-spec",         dest="data_spec", help="specification for training data (in, out, in_out) [default: %default]")
	parser.add_option("-m", "--model-dir",         dest="model_dir", help="directory to save the best models [default: %default]")

#	parser.add_option("-r", "--train-file",        dest="featFile_train")
#	parser.add_option("-s", "--test-file",         dest="featFile_test")
#	parser.add_option("-v", "--validation-file",   dest="featFile_validate")

	# network related
	parser.add_option("-t", "--max-tweet-length",  dest="maxlen",       type="int", help="maximul tweet length (for fixed size input) [default: %default]") # input size

	parser.add_option("-F", "--nb_filter",         dest="nb_filter",     type="int",   help="nb of filter to be applied in convolution over words [default: %default]") # uni, bi-directional
	parser.add_option("-r", "--filter_length",     dest="filter_length", type="int",   help="length of neighborhood in words [default: %default]") # lstm, gru, simpleRNN
	parser.add_option("-p", "--pool_length",       dest="pool_length",   type="int",   help="length for max pooling [default: %default]") # lstm, gru, simpleRNN
	parser.add_option("-v", "--vocabulary-size",   dest="max_features",  type="float",   help="vocabulary size in percentage [default: %default]") # emb matrix row size
	parser.add_option("-e", "--emb-size",          dest="emb_size",      type="int",   help="dimension of embedding [default: %default]") # emb matrix col size
	parser.add_option("-s", "--hidden-size",       dest="hidden_size",   type="int",   help="hidden layer size [default: %default]") # size of the hidden layer
	parser.add_option("-o", "--dropout_ratio",     dest="dropout_ratio", type="float", help="ratio of cells to drop out [default: %default]")

	parser.add_option("-i", "--init-type",         dest="init_type",     help="random or pretrained [default: %default]") 
	parser.add_option("-f", "--emb-file",          dest="emb_file",      help="file containing the word vectors [default: %default]") 
	parser.add_option("-P", "--tune-emb",          dest="tune_emb",      action="store_false", help="DON't tune word embeddings [default: %default]") 

	#learning related
	parser.add_option("-a", "--learning-algorithm", dest="learn_alg", help="optimization algorithm (adam, sgd, adagrad, rmsprop, adadelta) [default: %default]")
	parser.add_option("-b", "--minibatch-size",     dest="minibatch_size", type="int", help="minibatch size [default: %default]")
	parser.add_option("-l", "--loss",               dest="loss", help="loss type (hinge, squared_hinge, binary_crossentropy) [default: %default]")
	parser.add_option("-n", "--epochs",             dest="epochs", type="int", help="nb of epochs [default: %default]")


	parser.set_defaults(
#    	data_dir        = "../data/"
    	data_dir        = "../data/earthquakes/in/"
    	,data_spec       = "in"
	    ,log_file       = "log"
    	,model_dir      = "./saved_models/"

#    	,featFile_train = "../data/good_vs_bad/CQA-QL-train.xml.multi.csv.feat"
#    	,featFile_test  = "../data/good_vs_bad/CQA-QL-test.xml.multi.csv.feat"
#    	,featFile_validate   = "../data/good_vs_bad/CQA-QL-validateel.xml.multi.csv.feat"

	   	,learn_alg      = "adam" # sgd, adagrad, rmsprop, adadelta, adam (default)   #-----------------Quan sua  adadelta--> sgd
	   	,loss           = "binary_crossentropy" # hinge, squared_hinge, binary_crossentropy (default)
	    ,minibatch_size = 128  #-quan sua 32-->128
    	,dropout_ratio  = 0.0

    	,maxlen         = 100
    	,epochs         = 25   #-quan sua 25-->100
    	,max_features   = 80
    	,emb_size       = 128
    	,hidden_size    = 128
    	,nb_filter      = 250
    	,filter_length  = 3 
    	,pool_length    = 2 
    	,init_type      = 'random' 
    	,emb_file       = "../data/unlabeled_corpus.vec"
    	,tune_emb       = True
	)

	(options,args) = parser.parse_args()


	#print('Loading data...')
	print('LOADING DATA...')
	print('----------------------------------------------------------------')
	input_="rt usrId rashid plz share widely rss diverted funds from uk meant for gujarat earthquake relief to fund shakha activities ! https"
	X_newinput= aidr2.load_and_numberize_data2(path=options.data_dir,path=options.data_dir, nb_words=options.max_features, init_type=options.init_type, embfile=options.emb_file, validate_train_merge=0, map_labels_to_five_class=0)


	X_newinput  = sequence.pad_sequences(X_newinput,  maxlen=options.maxlen)#Quan them vao--------------------
        #print(X_train[0]) #quan them vao

	#build model...
#	nb_classes = np.max(y_train) + 1
        nb_classes=2
	if nb_classes == 2: # binary
		loss       = options.loss
		#class_mode = "binary"
		optimizer  = options.learn_alg
#
	elif nb_classes > 2: # multi-class
		loss       = 'categorical_crossentropy'
		#class_mode = 'categorical'
		optimizer  = options.learn_alg
		print("** optimizer: " + options.learn_alg)	
		# convert class vectors to binary class matrices [ 1 of K encoding]



#######################LOAD MODEL ###########################################
	model_name = options.model_dir + "cnn" + "-" + optimizer + "-" + str(options.nb_filter) + "-" + str(options.filter_length) + \
        "-" + str(options.pool_length) + "-" + str (options.tune_emb) +\
	"-" + loss + "-" + str (options.minibatch_size) + "-" + str(options.dropout_ratio) + "-init-" + str (options.init_type) + "-" +\
	str (options.max_features) + "-" + str (options.emb_size) + "-" + str (options.hidden_size) + ".model.cl." + str(nb_classes) + ".dom." + str(options.data_spec) 

	model = model_from_json(open(model_name + ".json").read())
        model.load_weights(model_name+".h5")
        
	model.compile(optimizer=optimizer, loss=loss, metrics=["accuracy"] )#,  class_mode=class_mode) #--Quan bo class_mode=calss_mosde va them metrics=["accuracy"]
        y_newinput_pred = model.predict_classes(X_newinput,batch_size=1024)
	print("INPUT: "+ str(len(X_newinput)))
	print("INPUTlabelPred: "+ str(len(y_newinput_pred)))
	print("The last date and time EXECUTED: " , datetime.datetime.now())	

	with open("LabelPred.csv", "w") as t:
        	writer = csv.writer(t)
        	writer.writerows(y_newinput_pred)



###################################################################
	





