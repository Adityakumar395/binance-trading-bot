import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_binance_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    # Connection logic - testnet=True assignment requirement hai
    client = Client(api_key, api_secret, testnet=True)
    return client