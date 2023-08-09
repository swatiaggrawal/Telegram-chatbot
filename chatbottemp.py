# -*- coding: utf-8 -*-

!pip install python-telegram-bot==13.7

!pip install pandas_datareader

!pip install yfinance

import telegram.ext
import pandas_datareader as web
import yfinance as yf

TOKEN = 'enter your token name'

def start(update, context):
  update.message.reply_text("WELCOME.")

def help(update, context):
  update.message.reply_text("""
  /start->Welcome
  /help->get help
  /content->Info about this bot
  /contact->contact info
  """)

def content(update, context):
  update.message.reply_text("temp")

def contact(update, context):
  update.message.reply_text("no contacts present")

def handle_message(update,context):
  update.message.reply_text(f"You said {update.message.text}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

def stock(update, context):
    if not context.args:
        update.message.reply_text("Please provide a stock ticker symbol.")
        return

    ticker = context.args[0]
    try:
        data = yf.download(ticker, period="1d")  # yfinance API for downloading data
        price = data.iloc[-1]['Close']
        update.message.reply_text(f"The current price of {ticker} is {price:.2f}$")
    except Exception as e:
        update.message.reply_text(f"Error fetching stock data: {e}")

disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("help",help))
disp.add_handler(telegram.ext.CommandHandler("content",content))
disp.add_handler(telegram.ext.CommandHandler("contact",contact))
disp.add_handler(telegram.ext.CommandHandler("stock",stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handle_message))

updater.start_polling()
updater.idle()