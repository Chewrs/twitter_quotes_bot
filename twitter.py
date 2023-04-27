# Importing the library
import tweepy  # pip3 install tweepy
import time
import requests  # pipe install requests
import config as C
import quotes as Q

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(
    C.BEARER_TOKEN, C.API_KEY, C.API_SECRET, C.ACCESS_TOKEN, C.ACCESS_TOKEN_SECRET
)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(
    C.API_KEY, C.API_SECRET, C.ACCESS_TOKEN, C.ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)


# set the text to tweet
def tweets():
    quote_text, author_text = Q.quotes_d()
    client.create_tweet(
        text=f'"{quote_text}" - {author_text} \n \n #quotes #programming #bot #API #Python'
    )
    date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    print(f"Tweet {date_time}")


# loop to tweet every hour
while 1:
    try:
        tweets()
        loop_int = int(C.TIME_FOR_NEXT_TWEET_IN_SECONDS)
        time.sleep(loop_int)  # 3600s = 1h
    except:
        continue
