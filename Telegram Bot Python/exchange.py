import json
import requests

# Principal values:
#  USD, RON, RUB, EUR, GBP, JPY
def test_value_api(from_val):
    url = 'https://api.exchangerate-api.com/v4/latest/' + str(from_val)
    try:
        response = requests.get(url)
        data = response.json()
        if json.dumps(data['result']) == "error":
            return False
        else:
            return True
    except:
        return True

def get_valut(from_val, to_val):
    url = 'https://api.exchangerate-api.com/v4/latest/' + str(from_val)   
    try:
        response = requests.get(url)
        data = response.json()
        return json.dumps(data['rates'][to_val], indent=4 )
    except:
        return "An error ocured. Please try another valute"
    

#print(get_valut("USD", "RON"))
