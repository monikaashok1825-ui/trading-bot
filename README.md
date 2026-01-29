## Note on Binance Futures Testnet Access

At the time of implementation, Binance Futures Testnet API access was restricted and redirected to Binance Demo Trading (UI-only), which does not support API-based order placement.

The application is implemented against the official Binance Futures Testnet endpoint (`https://testnet.binancefuture.com`) with full request construction, validation, logging, and error handling.

Due to the platform restriction, live order execution could not be completed; however, the application correctly handles request flow, API interaction, and error responses as expected.
