import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import *

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

# Validation
symbol = validate_symbol(args.symbol)
side = validate_side(args.side)
order_type = validate_order_type(args.type)
quantity = validate_quantity(args.quantity)
price = validate_price(args.price, order_type)

# Order placement
if order_type == "MARKET":

    order = place_market_order(
        symbol,
        side,
        quantity
    )

elif order_type == "LIMIT":

    order = place_limit_order(
        symbol,
        side,
        quantity,
        price
    )

print("Order Response:", order)