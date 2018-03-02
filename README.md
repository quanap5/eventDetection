# Event Detection Demonstration [here](https://github.com/quanap5/eventDetection/blob/master/Readme.pdf)

- Using deepleaning technique for real-time event detection
  - CNN: identify informative data
  - LSTM: temporal event detetection (earthquake data is used for demo)
- Introduction
We  designed  a  Graphic  User  Interface  usingPyQt. Both CNN  model and LSTM  model are built in Python using Keras deep learning library. Because the deep models can take a long time totrain,  we  should  pre-train  them  for  saving  andthen  load  them  again  for  use.  We  can  use  tabtraining  CNN  or  RNN  to  retrain  them.  The following interfaces are tabs for setting and some modes of our application such as a configuration tab for keywords, set the language for streaming tweets,  set  name,  and  some  other  informations. Also, the display  list  of  the  informative tweet  and  other  is  the  list  of  non-informative tweet coming with information about time. Thelast   sub-figure   is   real-time   plotting   ofaccumulated frequency keyword-related tweets, predicted  values,  and  earthquake  candidate underlying time series data.

----
## Requirement

- python
- tensorflow
- keras
- pyqt4

----
## Running

### Step1: clone this sourcecode to your local repository
- git clone https://github.com/quanap5/eventDetection

### Step2: Download word-embeddings for CNN model
- Download from website: https://nlp.stanford.edu/projects/glove/
- This configure for embedding with 200 of dimensionality namelly: glove_twitter_27B_200d.text
- Add to folder /embedings/

### Step 3 Run with GUI
-python demo.try

