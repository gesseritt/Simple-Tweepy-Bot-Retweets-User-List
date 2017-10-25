import tweepy
import random
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tweeted = []

tweets = api.list_timeline('username', 'username-listname')

def retweettwitterlist():
    while True:
        for tweet in tweets:
            if tweet.id not in tweeted:
                tweeted.append(tweet.id)
                api.retweet(tweet.id)
            elif tweet.id in tweeted:
                pass
        while len(tweeted) > 100:
            tweeted.clear()

retweettwitterlist()
