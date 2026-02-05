from binance.enums import *
from logging_config import logger

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity,
        }
        
        if order_type.upper() == 'LIMIT':
            if not price:
                return {"error": "Price is required for LIMIT orders"}
            params['price'] = str(price)
            params['timeInForce'] = TIME_IN_FORCE_GTC

        # Futures order place karna
        response = client.futures_create_order(**params)
        logger.info(f"SUCCESS: Order Placed {side} {quantity} {symbol}")
        return response

    except Exception as e:
        logger.error(f"FAILED: Order Failed: {str(e)}")
        return {"error": str(e)}