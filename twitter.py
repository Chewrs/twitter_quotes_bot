# Importing the library
import tweepy  # pip3 install tweepy
import time
import requests  # pipe install requests

# insert you keys
api_key = "*************************"
api_secret = "**************************************************"
bearer_token = r"****************************************************************************************************************"
access_token = "**************************************************"
access_token_secret = "*********************************************"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(
    bearer_token, api_key, api_secret, access_token, access_token_secret
)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# get the quotes from ninjas api
def quotes_d():
    global quote
    category = "computers"
    api_url = "https://api.api-ninjas.com/v1/quotes?category={}&limit=1".format(
        category
    )
    response = requests.get(
        api_url, headers={"X-Api-Key": "vk47EpqwD07BnO+nL8O4Gg==CoPeTzJTrksmlvHq"}
    )
    if response.status_code == requests.codes.ok:
        quotes = response.json()
        quote = quotes[0]["quote"]
        author = quotes[0]["author"]
        return quote, author
    else:
        print("Error:", response.status_code, response.text)


# set the text to tweet
def tweets():
    global quote
    quote_text, author_text = quotes_d()
    client.create_tweet(
        text=f'"{quote_text}" - {author_text} \n \n #quotes #programming #bot #API #Python'
    )
    date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    print(f"Tweet {date_time}")


# loop to tweet every hour
while 1:
    try:
        tweets()
        time.sleep(3600)  # 3600s = 1h
    except:
        continue
