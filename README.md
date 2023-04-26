# My Tweets Bot
My Tweets Bot is a simple Twitter bot that automatically tweets quotes every hour. It's written in Python and uses the tweepy library to interact with the Twitter API. The quotes are fetched from the Ninjas API.

## Installation
To use My Tweets Bot, you'll need to have Python 3.x installed on your system. You can install the required dependencies by running the following command in your terminal:

```sh
pip install tweepy

```
## Usage
Before using My Tweets Bot, you'll need to create a new Twitter app and obtain your API keys and access tokens. You can do this by following the Twitter Developer Documentation and creating a new app.

Next, you'll need to obtain an API key from the Ninjas API. You can sign up for a free account and get an API key [here](https://api-ninjas.com/).

Once you have your API keys and access tokens, you can clone this repository and add them to the [config.py](https://github.com/Chewrs/twitter_quotes_bot/blob/main/config.py) file. Replace the placeholders with your own keys and tokens:

```python
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
BEARER_TOKEN = r"your=bearer_token_here"
ACCESS_TOKEN = "your_access_token_here"
ACCESS_TOKEN_SECRET = "your_access_token_secret_here"
NINJAS_KEY = "your_ninjas_api_key_here"

```

After setting up your API keys and access tokens, you can run the bot by running the following command in your terminal:

```sh
python twitter.py
```
The bot will automatically tweet a new quote every hour. You can modify the list of quotes to include your own favorite quotes.

## Contributing
[CHE](https://chewrs.netlify.app/)

## License
My Tweets Bot is licensed under the [MIT License](https://github.com/Chewrs/twitter_quotes_bot/blob/main/LICENSE). Feel free to use and modify the code as you like.

## Acknowledgements

My Tweets Bot was inspired by [this tutorial](https://www.youtube.com/watch?v=BdmUhQnPToM) on building a Twitter bot with Tweepy. Thanks for the great tutorial! 

Additionally, I would like to thank ChatGPT for their assistance in helping me create this README file. 
