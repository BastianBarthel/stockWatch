import os
import requests
from twilio.rest import Client


# Company and stock name for the APIs, change if you want to track another stock
STOCK_NAME = "TSLA"
COMPANY_NAME = "tesla"
# API endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# API keys, set via environment variables
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
# Twilio keys, set via environment variables
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
# Phone number the messages are sent from, set via environment variables (needs to be registered in your Twilio account)
PHONE_NUMBER_FROM = os.environ.get("PHONE_NUMBER_FROM")
# Phone number the messages are sent to, set via environment variables (needs to be registered in your Twilio account)
PHONE_NUMBER_TO = os.environ.get("PHONE_NUMBER_TO")

UP = "🔺"
DOWN = "🔻"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

news_params = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": NEWS_API_KEY,
}


def send_sms(news: int):
    if yesterday_closing_price > day_before_yesterday_closing_price:
        symbol = UP
    else:
        symbol = DOWN

    text = f"{STOCK_NAME}: {symbol} {round(delta_percent, 2)}%\nHeadline: {news_list[news][0]}\nBrief: {news_list[news][1]}"
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body=text,
        from_=PHONE_NUMBER_FROM,
        to=PHONE_NUMBER_TO
    )


stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]
yesterday_closing_price = stock_list[0]["4. close"]
day_before_yesterday_closing_price = stock_list[1]["4. close"]
delta = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
delta_percent = delta / float(yesterday_closing_price) * 100

if delta_percent > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    news_list = [(news["title"], news["description"]) for news in news_data]

    for n in range(3):
        send_sms(n)
