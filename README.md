## Note on Binance Futures Testnet Access

At the time of implementation, Binance Futures Testnet API access was restricted and redirected to Binance Demo Trading (UI-only), which does not support API-based order placement.

The application is implemented against the official Binance Futures Testnet endpoint (`https://testnet.binancefuture.com`) with full request construction, validation, logging, and error handling.

Due to the platform restriction, live order execution could not be completed; however, the application correctly handles request flow, API interaction, and error responses as expected.


## API Setup Instructions
## API Setup Instructions

1. Create a Binance account (if not already available).

2. Attempt to access Binance Futures Testnet using:
   https://testnet.binancefuture.com

   Note:
   Binance currently redirects Futures Testnet access to Demo Trading (UI-only) for many users, which does not support API-based order placement.

3. Generate API credentials from the Futures Testnet API Management page (if accessible):
   - API Key
   - Secret Key
   - Enable Futures permission

4. Store API credentials securely using environment variables.
   Create a `.env` file in the project root:

   BINANCE_API_KEY=your_api_key_here  
   BINANCE_API_SECRET=your_secret_key_here

5. Do NOT commit the `.env` file to GitHub.


## How to run the Bot (CLI Usage)
## How to Run the Bot

### 1. Install Dependencies

```bash
pip install -r requirements.txt

## 2. Run a market order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001


## 3. Run a Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000


CLI Parameters

symbol : Trading pair (e.g., BTCUSDT)

side : BUY or SELL

type : MARKET or LIMIT

quantity : Order quantity

price : Required only for LIMIT orders


---

## Logging

```markdown
## Logging

All API requests, responses, and errors are logged to:

logs/trading_bot.log

The log file contains:
- Market order request & response
- Limit order request & response
- Error handling information

## Important Note on Testnet Limitation
## Testnet Limitation Notice

At the time of implementation, Binance Futures Testnet API access was restricted and redirected to Binance Demo Trading (UI-only), which does not support API-based order execution.

The bot is implemented against the official Futures Testnet endpoint with complete request construction, validation, logging, and exception handling.
