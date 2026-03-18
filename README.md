# TRADING_BOT
A Python CLI-based trading bot that places Market and Limit orders on Binance Futures Testnet with input validation, logging, and error handling.

Binance Futures Trading Bot (Testnet)

Overview

This project is a Python CLI-based trading bot that places orders on the Binance Futures Testnet (USDT-M).
The bot supports both Market and Limit orders and accepts user input through the command line.

This project was developed as part of a Python Developer Internship assignment.

⸻

Features
	•	Place Market Orders
	•	Place Limit Orders
	•	Supports BUY and SELL
	•	Command Line Interface (CLI)
	•	Input validation
	•	Structured project architecture
	•	Error handling
	•	Logging support

⸻

**Project Structure**
trading_bot
│
├── bot
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
└── README.md

**Requirements**

pip install -r requirements.txt


Binance Testnet Setup
	1.	Go to Binance Futures Testnet
https://testnet.binancefuture.com
	2.	Create an account.
	3.	Generate API credentials from API Management.
	4.	Add your API credentials in client.py.

  API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_SECRET_KEY"


**Run the Bot**

Open terminal in the project directory.

**Market Order**
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

**Limit Order**
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
