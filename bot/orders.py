from binance.exceptions import BinanceAPIException
from bot.validators import validate_inputs
from bot.logging_config import logger


def place_trade(client, symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)

    # ===== ORDER REQUEST SUMMARY =====
    print("\n===== ORDER REQUEST SUMMARY =====")
    print(f"Symbol       : {symbol}")
    print(f"Side         : {side}")
    print(f"Order Type   : {order_type}")
    print(f"Quantity     : {quantity}")
    if order_type == "LIMIT":
        print(f"Price        : {price}")

    order = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        order["price"] = price
        order["timeInForce"] = "GTC"

    try:
        response = client.place_order(**order)

        print("\n===== ORDER RESPONSE =====")

        if "orderId" in response:
            print(f"Order ID     : {response.get('orderId')}")
            print(f"Status       : {response.get('status')}")
            print(f"Executed Qty : {response.get('executedQty')}")
            print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")
            print("\n✅ Order placed successfully")
        else:
            print("❌ Order failed")
            print("Error Code   :", response.get("code"))
            print("Error Message:", response.get("msg"))

    except BinanceAPIException as e:
     print("\n===== ORDER RESPONSE =====")
     print("❌ Order failed")
     print("Error Code   :", e.code)
     print("Error Message:", e.message)

    except Exception as e:
     print("\n===== ORDER RESPONSE =====")
     print("❌ Order failed due to unexpected error")
     print(str(e))



