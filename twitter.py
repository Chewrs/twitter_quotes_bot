# Importing Tweepy
import tweepy
import time
import requests

# Credentials
api_key = "6qz66iWIalpc5vjQ1pDkfvSFx"
api_secret = "VZX6T43VdmXIAodGUE0OhJz9Cy8BlJye6zw0GJE2lmFAPZYMz5"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAANRqmwEAAAAAFVaa9GRaomdYveKzRPseRsIiuaw%3DvIDZEZ349D6m0tlGEGH1QrtTWS5AzPDD31xlFnd8qu03s2PeY8"
access_token = "1459517200788705283-TfEDZgnt2pwxy8LZuH4NmdwMw9mO5K"
access_token_secret = "sgK2aZqUqDprpH2R1Zz6Ihs540cP3hpnmBPiuctRbVLD2"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(
    bearer_token, api_key, api_secret, access_token, access_token_secret
)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


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


# Creating a tweet to test the bot


def tweets():
    global quote
    quote_text, author_text = quotes_d()
    client.create_tweet(
        text=f'"{quote_text}" - {author_text} \n \n #quotes #programming #bot #API #Python'
    )
    date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
    print(f"Tweet {date_time}")


while 1:
    try:
        tweets()
        time.sleep(3600)
    except:
        continue
