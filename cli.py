import argparse
from bot_client import get_binance_client
from orders import place_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    parser.add_argument('--symbol', required=True, help="e.g. BTCUSDT")
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL'])
    parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT'])
    parser.add_argument('--qty', required=True, type=float)
    parser.add_argument('--price', type=float, help="Required for LIMIT orders")

    args = parser.parse_args()
    
    client = get_binance_client()
    
    # Order execute karna
    place_order(client, args.symbol, args.side, args.type, args.qty, args.price)

if __name__ == "__main__":
    main()