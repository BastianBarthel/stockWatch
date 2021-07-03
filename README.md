# stockWatch

A Python script that checks the last two closing courses of a stock and sends sms with the latest news articles related to the company to your phone if the delta is > 5%

## Instructions:

Register to get the following free API keys:
https://www.alphavantage.co/
https://newsapi.org/
Get a free Twilio account:
https://www.twilio.com/

Set the following environment variables:
STOCK_API_KEY (Alpha Vantage key)
NEWS_API_KEY (News API key)
ACCOUNT_SID (Twilio account sid)
AUTH_TOKEN (Twilio auth token)
PHONE_NUMBER_FROM (Twilio phone number)
PHONE_NUMBER_TO (Your phone number)

How to get Twilio to work on free PythonAnywhere accounts:
https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/