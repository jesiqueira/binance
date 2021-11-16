from binance.spot import Spot as Client
from config import Config

client = Client(base_url='https://testnet.binance.vision', key=Config.API_KEY, secret=Config.API_SECRET)
print(client.time())

# client = Spot(key=Config.API_KEY, secret=Config.API_SECRET)

# Get account information
print(client.account())