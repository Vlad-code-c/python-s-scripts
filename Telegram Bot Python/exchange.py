import json
import requests

# Where USD is the base currency you want to use
url = 'https://api.exchangerate-api.com/v4/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()


print(json.dumps(data['rates']['USD'], indent=4 ))


    