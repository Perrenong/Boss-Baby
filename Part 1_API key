import requests
api_key = "71RDX3LKNAQLVGYO"
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=71RDX3LKNAQLVGYO"

response = requests.get(url)
print(response)
print(response.headers)

print(response)
import json 
data = response.json()
print(json.dumps (data, indent = 4 ))
