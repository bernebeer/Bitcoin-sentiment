import tweepy
from tweepy import OAuthHandler

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# Get twitter app key credentials from external file
from dev_settings import *

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):

    def on_data(self, data):
        print(data)
        try:
            with open('bitcoin-tweets.json', 'a') as f:
                f.write(data)
                # print("printed")
                return True
        except BaseException as e:
            print(str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['litecoin'])