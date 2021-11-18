from binance.client import Client
from time import sleep
from binance import ThreadedDepthCacheManager
from config import Config
import pprint


client = Client(Config.API_KEY, Config.API_SECRET)
client.API_URL = 'https://testnet.binance.vision/api'

# Informações da conta
# print(client.get_account())

# Preço mais recente do Bitcoin
btc_price = client.get_symbol_ticker(symbol='BTCUSDT')
# print(btc_price)

def btc_trade_history(msg):
    '''definir como processar mensagens WebSocket recebidas '''

    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['ask'] = msg['a']
        btc_price['error'] = False
    else:
        btc_price['error'] = True

bsm = ThreadedDepthCacheManager()
bsm.start()

# subscribe to a stream
bsm.start_symbol_ticker_socket(callback=btc_trade_history, symbol='BTCUSDT')

# stop websocket