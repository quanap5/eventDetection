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


model=lm.load_model()

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser


class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_dir, query):
        query_fname = format_filename(query)
        self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)

    def on_data(self, data):
	#global model
        try:
            with open(self.outfile, 'a') as f:
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


#			t0 = time.clock()
#			X_newinput= aidr2.load_and_numberize_data2(input_tweet,path=data_dir, nb_words=max_features, init_type=init_type, embfile=emb_file, validate_train_merge=0, #map_labels_to_five_class=0)
#			print ("Thoi gian map to vector ", time.clock() - t0)
#			print ( X_newinput) 
#			X_newinput  = sequence.pad_sequences(X_newinput,  maxlen)#Quan them vao--------------------
		        return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True


def format_filename(fname):
    """Convert file name into a safe string.

    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.

    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

if __name__ == '__main__':
    
    parser = get_parser()
    args = parser.parse_args()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)


    

    twitter_stream = Stream(auth, MyListener(args.data_dir, args.query))
    #twitter_stream.filter(track=[args.query])
    twitter_stream.filter(track=['earthquake'])
#,'quake','terremoto','maremoto','gempa','tsunami','deprem','zelzele','lindol'])
    #twitter_stream.filter(locations=[124, 33, 130, 38])#GEO_KOREA
    #twitter_stream.filter(locations=[-180, -90, 180, 90])#GEO_WORLD
