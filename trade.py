import requests
from enum import Enum
from datetime import datetime, timedelta

class TimespanType(Enum): 
    second = "second", 
    minute = "minute", 
    hour = "hour",
    day = "day", 
    week = "week",
    month = "month",
    quater = "quater", 
    year = "year"

class MarketType(Enum): 
    stocks = "stocks", 
    crypto = "crypto",
    fx = "fx",
    otc = "otc", 
    indices = "indices"


class TraderService(): 
    _baseUrl:str = "https://api.polygon.io/"
    _accessToken:str

    def __init__(self, accessToken:str):
        self._accessToken = accessToken

    def GetTradeData(self, symbol: str, multiplier:int, timespanType:TimespanType) -> any: 
        currentDt:datetime = datetime.now()
        pastDt:datetime = currentDt + timedelta(days=-5)
        
        json = self.mkRequest(f"v2/aggs/ticker/{symbol}/range/{multiplier}/{timespanType.name}/{pastDt.strftime(r"%Y-%m-%d")}/{currentDt.strftime(r"%Y-%m-%d")}")

        return json
            
    def GetTickerData(self, symbol: str) -> any: 
        json = self.mkRequest(f"v3/reference/tickers/{symbol}")

        return json
    
    def GetTickers(self, market: MarketType) -> any:         
        json = self.mkRequest(f"v3/reference/tickers?market={market.name}&sort=name&limit=1000")

        return json
            
    def mkRequest(self, endpoint:str): 
        headers = {
            'Authorization': f'Bearer {self._accessToken}',
            'Content-Type': 'application/json'
        }

        url:str = f"{self._baseUrl}{endpoint}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200: 
            return response.json()
        else: 
            print(f'Request failed with status code: {response.status_code}\nResponse Content: {response.json()}')

