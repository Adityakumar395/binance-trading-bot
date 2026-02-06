**Binance Futures Trading Bot (Testnet)**

​A Python-based Command Line Interface (CLI) application designed to automate Market and Limit orders on the Binance Futures Testnet (USDT-M). 
This project demonstrates modular software design, secure API integration, and structured logging practices.

**​Key Features**

**​Order Versatility:** Supports both MARKET and LIMIT order types.

**​Side Support:** Fully functional for both BUY and SELL operations.

**​Structured Logging:** Detailed logs of every transaction and error are maintained in bot.log for auditing.

**​Security Focused:** Environment-based configuration using .env files to protect sensitive API credentials.

**Setup & Installation**

**1. Clone the Repository:** git clone https://github.com/Adityakumar395/binance-trading-bot.git

   cd binance-trading-bot
   
**2. Install Dependencies:** pip install -r requirements.txt(Dependencies include python-binance and python-dotenv)

**3. Environment Configuration:** Create a file named .env in the root directory and add your Binance Testnet keys.

   BINANCE_API_KEY=your_testnet_api_key
   
   BINANCE_API_SECRET=your_testnet_api_secret
   
   NOTE: The original .env file has been removed from GitHub for security compliance

**Usage Examples**

You can execute orders directory from your terminal using the following commands:

**1. Execute a MARKET BUY Order:**
   python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.1
   
**2. Execute a MARKET SELL Order:**
   python cli.py --symbol BTCUSDT --side SELL --type MARKET --qty 0.1

**3. Execute a LIMIT Buy Order:**
   python cli.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.1 --price 70000
   
   Note: For a Limit BUY order to be placed below the market, the specified price should be lower than the current market price.
   The order will be added to the order book and executed only when the market price drops to your specified level.)
   
**4. Execute a LIMIT SELL Order:**
   python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.1 --price 105000

   Note: For a Limit SELL order, the price should be higher than the current market price to ensure it executes at your desired profit target.
   


