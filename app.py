from credentials import ACCESS_KEY, ACCESS_SECRET
import tweepy
from time import sleep
import datetime
import os
from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET  = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'voz do xaropinho'
today = datetime.today().strftime('%Y-%m-%d')

for tweet in tweepy.Cursor(api.search, search, since = today).items():
    try:
        if tweet.author.screen_name != 'xaropinhobot' and not tweet.retweeted:
                print("@" + tweet.user.screen_name)
                tweet.favorite()
                reply = 'RAPÁÁÁZ ' + 'www.youtube.com/watch?v=whns12cw4-w&ab_channel=XaropinhoBot' 
                api.update_status(reply, tweet.id, auto_populate_reply_metadata=True)
                sleep(90)
    except tweepy.error.TweepError as e:
        pass
    except StopIteration:
        break