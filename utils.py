import requests


API_KEY = '7a30d95d34c619818512332d6506fb51'
BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'

def is_valid_currency(currency_code):
    response = requests.get(BASE_URL, params={'apikey': API_KEY})
    
    if response.status_code == 200:
        data = response.json()
        currencies = data['rates'].keys()
        
        return currency_code.upper() in currencies
    else:
        return False

def convert_currency(from_currency, to_currency, amount):
    response = requests.get(BASE_URL, params={'apikey': API_KEY})
    
    if response.status_code == 200:
        data = response.json()
        rates = data['rates']
        
        if from_currency.upper() in rates and to_currency.upper() in rates:
            conversion_rate = rates[to_currency.upper()] / rates[from_currency.upper()]
            converted_amount = amount * conversion_rate
            return converted_amount
        else:
            return None
    else:
        return None
