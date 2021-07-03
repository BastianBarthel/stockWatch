# stockWatch

A Python script that checks the last two closing courses of a stock and sends sms with the latest news articles related to the company to your phone if the delta is > 5%

## Instructions:

Register to get the following free API keys:<br>
https://www.alphavantage.co/<br>
https://newsapi.org/<br>

Get a free Twilio account:<br>
https://www.twilio.com/<br>

Set the following environment variables:<br>
STOCK_API_KEY (Alpha Vantage key)<br>
NEWS_API_KEY (News API key)<br>
ACCOUNT_SID (Twilio account sid)<br>
AUTH_TOKEN (Twilio auth token)<br>
PHONE_NUMBER_FROM (Twilio phone number)<br>
PHONE_NUMBER_TO (Your phone number)<br>

How to get Twilio to work on free PythonAnywhere accounts:<br>
https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
