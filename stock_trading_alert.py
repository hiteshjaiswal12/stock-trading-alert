import requests
from twilio.rest import Client

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'TESLA INC'

news_api = "c8115e17ecdd4ec588d676b7ed75f2f8"
stock_api = "LZTP3SMHSUJM1WBO"

stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"
twilio_sid = "ACe194146e8131a517a271e614769d8073"
twilio_auth_token = "006d02b99bb2fc088526697237383efa"

#step 1 : Get yesterday's closing stock price
stock_parameter = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":stock_api,
}
response = requests.get(stock_endpoint,params=stock_parameter)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

#STEP - 2 Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#STEP 3 - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20 , but the positive difference is 20.
difference = abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
print(difference)


#STEP 4 - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

#STEP 5 - IF diff_percent is greater than 5 then print("Get News")
if diff_percent > 0.3:
    print("Get News")

#STEP 6 - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME
if diff_percent > 0.3:
    news_parameter = {
        "apiKey":news_api,
        "qInTitle":COMPANY_NAME,
    }

    news_response = requests.get(news_endpoint,news_parameter)
    articles = news_response.json()['articles']
    #print(articles)

    #STEP-7 - Use Python slice operator to create a list that contains the first 3 articles.
    top_three_articles = articles[:3]
    print(top_three_articles)

# Use Twilio to send a separate message with each article's title and description to your phone number

#STEP - 8  Create a new list of the first 3 articles headline and description using list comprehension
"Headline: {article title}. \n Brief: {article description}"

formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in top_three_articles]
print(formatted_articles)

#STEP - 9 Send each article as a separate message via Twilio.
client = Client(twilio_sid,twilio_auth_token)

#STEP 10 - Send each article as a seperate message via Twilio
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_= "+16812442677",
        to="+916267285860"
    )










