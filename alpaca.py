from alpaca.trading.client import TradingClient

# API authentication info
API_KEY = "PKXF9WWBLOP0PDEX6HTB"
SECRET_KEY = "37lEr7zF002VrDaxjeQaub4D2TRxYcclSPKTRVbV"

# instantiate REST API
traingAPI = TradingClient(API_KEY, SECRET_KEY, paper=True)

# Getting account information and printing it
account = traingAPI.get_account()
for property_name, value in account:
  print(f"\"{property_name}\": {value}")