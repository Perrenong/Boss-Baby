import requests
import json 

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=71RDX3LKNAQLVGYO"

response = requests.get(url)
data = response.json()

"""
Get the exchange rate of  1 USD to SGD
"""
def get_exchange_rate():
    # data is type of dictionary

    # ['Realtime Currency Exchange Rate'] is the key the of dictionary
    # ['5. Exchange Rate'] is the key of the value of the dictionary
    return data['Realtime Currency Exchange Rate']['5. Exchange Rate']