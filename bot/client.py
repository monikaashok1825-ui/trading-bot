from binance.client import Client
from bot.logging_config import logger

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logger.info("Connected to Binance Futures Testnet")

    def place_order(self, **params):
     logger.info(f"Order Request: {params}")
     response = self.client.futures_create_order(**params)
     logger.info(f"Order Response: {response}")
     return response

