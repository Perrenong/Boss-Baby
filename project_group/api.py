import requests

#calling the program to an API
api_key = "71RDX3LKNAQLVGYO"
<<<<<<< HEAD
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=tage.co/query?function=FX_currency&from_symbol=USD&to_symbol=SGD&apikey=71RDX3LKNAQLVGYO"

response = requests.get(url)
print(response)
# print(response.headers)
=======
url = "https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=71RDX3LKNAQLVGYO"
#sends requests to a specific url
response = requests.get(url)
>>>>>>> 33e1e99e7f7b54815645d3c89c7ad85976c1ae4d

#returns a JSON object of the result
import json 
data = response.json()
print(data)
change US to Sg
# print(float(data["Time Series FX (Weekly)"]["2022-07-29"]["4. close"]))

<<<<<<< HEAD
# list = []
# for week, forex in data["Time Series FX (Weekly)"].items():
#     closing_price=(float(forex["4. close"]))
#     list.append(closing_price)
    
# average_forex_price = sum(list)/len(list)
# print(f"The mean of the weekly closing forex price is ${round(average_forex_price,2)}")
=======
#list to store collections of data
list = []
for week, forex in data["Time Series FX (Weekly)"].items():
    closing_price=(float(forex["4. close"]))
    list.append(closing_price)

 #calculating the mean of the weekly closing forex price   
average_forex_price = sum(list)/len(list)
print(f"The mean of the weekly closing forex price is ${round(average_forex_price,2)}")
>>>>>>> 33e1e99e7f7b54815645d3c89c7ad85976c1ae4d

