import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_converter(currency: str, amount: str):
    to = "RUB"
    from_currency = currency
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_currency}&amount={amount}"

    headers= {"apikey": os.getenv('API_KEY')}

    response = requests.get(url, headers=headers, data ={})

    return response.json().get("result")
