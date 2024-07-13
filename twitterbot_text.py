import tweepy
from time import sleep

# Import Twitter credentials from credentials.py
from credentials import *

    
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(
    access_token,
    access_token_secret,
)
api = tweepy.API(auth)
my_file=open('sample.txt','r')
file_lines=my_file.readlines()
my_file.close()

def tweet_text():
    for line in file_lines:
        try:
            print(line)
            if line != "\n":
                client.create_tweet(text=line)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)

def tweet_with_image():
    try:
        media_path = "./twitter_text_bot.png"
        media = api.media_upload(filename=media_path)
        media_id = media.media_id
        client.create_tweet(text="Tweet text", media_ids=[media_id])
    except tweepy.TweepError as e:
        print(e.reason)

tweet_with_image()

sleep(10)