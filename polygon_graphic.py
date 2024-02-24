import sys
from trade import TraderService, TimespanType, MarketType
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import pandas as pd
import requests
import xlsxwriter
import math 
from secret import POLYGON_API_KEY
import datetime
import plotly.graph_objects as grphObj
from plotly.subplots import make_subplots

class Trader:
    _traderService:TraderService

    def __init__(self):



        symbol:str = "C:AUDUSD" #input("Stock Symbol: ") 
        self._traderService = TraderService(POLYGON_API_KEY)

        # tickersJson = self._traderService.GetTickers(MarketType.fx)
        # print(tickersJson)

        # for ticker in tickersJson['results']: 
        #     print(ticker['ticker'], ticker['name'])

        tradeJson = self._traderService.GetTradeData(symbol, 5, TimespanType.minute)
        # json = self._traderService.GetTickerData(symbol)

        df = pd.DataFrame(columns = ['volume', 'weighted_volume', 'open', 'close', 'high', 'low', 'timestamp', 'transactions'])

        if (tradeJson['results'] != []):
            for result in tradeJson['results']: 
                df.loc[len(df)] = [
                    result['v'], 
                    result['vw'], 
                    result['o'], 
                    result['c'], 
                    result['h'], 
                    result['l'], 
                    datetime.datetime.fromtimestamp(float(result['t'])/1000, datetime.timezone(datetime.timedelta(hours=10))), 
                    result['n'], 
                ]

        # fig = grphObj.Figure(data=grphObj.Scatter(x=df["timestamp"],y=df['close'], mode='lines'))
        # fig.show()

        df['diff'] = df['close'] - df['open']
        df.loc[df['diff']>=0, 'color'] = 'green'
        df.loc[df['diff']<0, 'color'] = 'red'

        fig3 = make_subplots(specs=[[{"secondary_y": True}]])
        fig3.add_trace(grphObj.Candlestick(x=df.index,
                                    open=df['open'],
                                    high=df['high'],
                                    low=df['low'],
                                    close=df['close'],
                                    name='Price'))
        fig3.add_trace(grphObj.Scatter(x=df.index,y=df['close'].rolling(window=20).mean(),marker_color='blue',name='20 Day MA'))
        fig3.add_trace(grphObj.Bar(x=df.index, y=df['volume'], name='volume', marker={'color':df['color']}),secondary_y=True)
        fig3.update_yaxes(range=[0,700000000],secondary_y=True)
        fig3.update_yaxes(visible=False, secondary_y=True)
        fig3.update_layout(xaxis_rangeslider_visible=False)  #hide range slider
        fig3.update_layout(title={'text':symbol, 'x':0.5})
        fig3.show()


if __name__ == "__main__":
    t = Trader()
