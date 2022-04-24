#!/usr/bin/env python3
from Globals import *

def updateTransactionSheetAfterBuy(symbol, amount, price, total_spending):
  with open(db_transaction_path, "a") as f:
      data = "\n"+"Buy,"+symbol+","+amount+","+price+","+","+","+"," + str(total_spending)
      f.write(data)
  return

def updateTransactionSheetAfterSell(symbol, amount, price, total_spending):
  with open(db_transaction_path, "a") as f:
      data = "\n"+"Sell,"+price+","+","+","+"," +symbol+","+amount+ "," + str(total_spending)
      f.write(data)
  return

def updateTransactionSheetAfterTrade(coin_sell, coin_buy):
  symbol_sell, amount_sell, price_sell, total_spending_sell = coin_sell
  symbol_buy, amount_buy, price_buy, total_spending_buy = coin_buy
  with open(db_transaction_path, "a") as f:
      data = "\n"+"Trade,"+symbol_buy+","+amount_buy+","+price_buy+","+symbol_sell+","+amount_sell+","+price_sell+"," \
             + str(total_spending_sell)
      f.write(data)
  return