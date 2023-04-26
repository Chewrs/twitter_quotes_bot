import requests
import config as C


# get the quotes from ninjas api
def quotes_d():
    global quote
    category = "computers"
    api_url = "https://api.api-ninjas.com/v1/quotes?category={}&limit=1".format(
        category
    )
    response = requests.get(api_url, headers={"X-Api-Key": C.NINJAS_KEY})
    if response.status_code == requests.codes.ok:
        quotes = response.json()
        quote = quotes[0]["quote"]
        author = quotes[0]["author"]
        return quote, author
    else:
        print("Error:", response.status_code, response.text)
