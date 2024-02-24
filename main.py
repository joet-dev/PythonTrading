import websocket
from websocket import create_connection
import threading 
import _thread as thread
import time
import json
import base64

stop_event = threading.Event()

ticker_list = {}

def onMessage(ws, message):
    print(message) 
    message_bytes = base64.b64decode(message)
    print(message_bytes)

def on_open(ws:websocket.WebSocketApp):
    symbol_list = {}
    symbol_list["subscribe"] = ['AMZN', 'MSFT']
    def run(*args):
        ws.send(json.dumps(symbol_list))

    thread.start_new_thread(run, ())
    print("### connection is open ###")

ws = websocket.WebSocketApp(
    "wss://streamer.finance.yahoo.com/",
    on_message=onMessage
)
ws.on_open = on_open
ws.run_forever()



      
