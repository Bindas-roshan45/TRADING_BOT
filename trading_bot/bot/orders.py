from bot.client import client

def place_market_order(symbol, side, quantity):

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    return order


def place_limit_order(symbol, side, quantity, price):

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        timeInForce="GTC",
        quantity=quantity,
        price=price
    )

    return order