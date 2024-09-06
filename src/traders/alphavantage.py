import requests 
from enum import Enum 
from datetime import datetime


class AVFunction(Enum): 
    TIME_SERIES_INTRADAY = 0


class AlphaVantageService:
    base_url = "https://www.alphavantage.co/query"
    def __init__(self, api_key:str):
        self.api_key = api_key

    def getStockData(self, function:AVFunction, symbol:str, interval:str = 5, outputsize:str = "compact", hist_month:datetime = None, adjusted:bool = True):
        params = {
            "function": function.name,
            "symbol": symbol,
            "interval": f"{interval}min",
            "outputsize": outputsize,
            "apikey": self.api_key,
            "adjusted": adjusted
        }

        if (hist_month is not None):
            params["month"] = hist_month.strftime("%Y-%m")

        response = requests.get(self.base_url, params=params)
        return response.json()
