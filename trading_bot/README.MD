Binance Futures Trading Bot (Testnet)

Overview

This project is a simple Python CLI-based trading bot that places orders on the Binance Futures Testnet (USDT-M).
It supports both Market and Limit orders and demonstrates a clean project structure with input validation, logging, and error handling.

This application is designed as part of a Python Developer Internship Assignment.

⸻

Features
	•	Place Market Orders
	•	Place Limit Orders
	•	Support for BUY and SELL sides
	•	CLI-based input using argparse
	•	Input validation
	•	Structured code architecture
	•	Logging for API requests and responses
	•	Error handling for invalid inputs and API errors

⸻

Project Structure

trading_bot/

bot/
    client.py → Binance API client configuration
    orders.py → Order placement logic
    validators.py → Input validation functions
    logging_config.py → Logging configuration

cli.py → Command Line Interface entry point
requirements.txt → Python dependencies
README.md → Project documentation

⸻

Requirements

Python 3.x

Required libraries:
	•	python-binance
	•	requests

Install dependencies using:

pip install -r requirements.txt

⸻

Binance Testnet Setup
	1.	Go to Binance Futures Testnet
https://testnet.binancefuture.com
	2.	Create an account or login.
	3.	Generate API credentials from API Management.
	4.	Add your API credentials in client.py.

Example:

API_KEY = “YOUR_API_KEY”
API_SECRET = “YOUR_SECRET_KEY”

Note: Never share your API credentials publicly.

⸻

How to Run

Open terminal in the project directory.

Market Order Example

python cli.py –symbol BTCUSDT –side BUY –type MARKET –quantity 0.002

Example Output:

Order Response:
orderId: 123456
status: FILLED

⸻

Limit Order Example

python cli.py –symbol BTCUSDT –side SELL –type LIMIT –quantity 0.002 –price 70000

Example Output:

Order Response:
orderId: 123457
status: NEW

⸻

Input Parameters

symbol → Trading pair (example: BTCUSDT)

side → BUY or SELL

type → MARKET or LIMIT

quantity → Order quantity

price → Required only for LIMIT orders

⸻

Logging

API requests, responses, and errors are logged for debugging and monitoring purposes.

Example log entry:

INFO Market order placed successfully
Symbol: BTCUSDT
Side: BUY

⸻

Error Handling

The application handles:
	•	Invalid user inputs
	•	Incorrect order parameters
	•	API errors from Binance
	•	Network issues

⸻

Assumptions
	•	Orders are placed only on Binance Futures Testnet
	•	API keys must be valid and enabled for Futures trading
	•	Minimum order size requirements must be respected

⸻

Author

Roshan Kumar
Python Developer Intern Applicant