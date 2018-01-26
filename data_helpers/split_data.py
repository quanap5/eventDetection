#!/usr/bin/python
#!/usr/bin/env python
#===================================================================================
#This file Earthquake project: split data set into training data, test data and 
#Editor: Nguyen Van Quan
#Date edit: 2016 Nov 06
#http://stats.stackexchange.com/questions/19048/what-is-the-difference-between-test-set-and-validation-set
#++Training set (60% of the original data set): This is used to build up our prediction algorithm. Our algorithm tries to tune itself # to the quirks of the training data sets. In this phase we usually create multiple algorithms in order to compare their performances # during the Cross-Validation Phase.
#
# ++Cross-Validation set (20% of the original data set): This data set is used to compare the performances of the prediction
# algorithms that were created based on the training set. We choose the algorithm that has the best performance.
#
# ++Test set (20% of the original data set): Now we have chosen our preferred prediction algorithm but we don't know yet how it's 
# going to perform on completely unseen real-world data. So, we apply our chosen prediction algorithm on our test set in order to see # how it's going to perform so we can have an idea about our algorithm's performance on unseen data.
#====================================================================================

#=================
#==> Libraries <==
#=================
import sys, os
import csv
import numpy as np
from sklearn.cross_validation import StratifiedKFold


#============
#==> Main <==
#============

#-----------------
#--> Load data <--
#-----------------
in_file=sys.argv[1]

with open(in_file, 'rU') as fin:
	i=np.array([])
	X=np.array([])
	y=np.array([])
        rows = csv.reader(fin)
	header = next(rows)
	for col in rows:
		i = np.append(i,col[0]) #tweet_id
		X = np.append(X,col[1]) #tweet
		y = np.append(y,col[2]) #label

#------------------------------------------
#--> split data into train+validate and test <--
#------------------------------------------
skf = StratifiedKFold(y, n_folds=5, shuffle=True) # n_folds = sum of train to validate to test ratio

for train_validate_index, test_index in skf:
	train_validate = zip(i[train_validate_index], X[train_validate_index], y[train_validate_index])
	test = zip(i[test_index], X[test_index], y[test_index])

#-----------------------------------------
#--> intermidate files: train+validate file <--
#-----------------------------------------
filename = os.path.splitext(in_file)[0]
filename = os.path.basename(filename)

with open("%s_train_validate.csv" %filename, "wb") as f:
	writer = csv.writer(f)
	writer.writerow(header)
	writer.writerows(train_validate)

#---------------------------
#--> load train_validate data <--
#---------------------------
with open("%s_train_validate.csv" %filename) as fin:
        ii=np.array([])
        XX=np.array([])
        yy=np.array([])
        rows = csv.reader(fin)
        header = next(rows)
        for col in rows:
                ii = np.append(ii,col[0]) #tweet_id
                XX = np.append(XX,col[1]) #tweet
                yy = np.append(yy,col[2]) #label

#------------------------------------------
#--> split train+validate into train and validate <--
#------------------------------------------

skf = StratifiedKFold(yy, n_folds=8, shuffle=True) # n_folds = sum of train to validate ratio (a/1->a+1)

for train_index, validate_index in skf:
        train = zip(ii[train_index], XX[train_index], yy[train_index])
        validate = zip(ii[validate_index], XX[validate_index], yy[validate_index])

#--------------------
#--> save outputs <--
#--------------------

with open("%s_train.csv" %filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(train)

with open("%s_validate.csv" %filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(validate)

with open("%s_test.csv" %filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(test)

#---------------------------------
#--> deleter intermidate files <--
#---------------------------------
