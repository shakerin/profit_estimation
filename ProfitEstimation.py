#!/usr/bin/env python3
"""
ProfitEstimation.

Usage:
  ProfitEstimation save (basic|crypto) [--type=(buy|trade|sell)]
  ProfitEstimation setup


Options:
  setup           run this command only first time for setup
  save            indicates some info will be saved for future use
  basic           indicates basic trading - where user buys
                  or sells cryptocurrency with fiat
  crypto          indicates crypto trading - where user buys
                  or sells cryptocurrency with another cryptocurrency
  buy             user bought cryptocurrency with fiat money
  sell            user sold cryptocurrency for fiat money
  trade           user traded one cryptocurrency for another

"""

import json
from docopt import docopt
from JsonExtract import *
from common_func import *
from datetime import date

db_path = "./trading_data.csv"
calc_path = "./calculated_trading_data.csv"
calc_path_header = "symbol, total amount holding, average per unit price, fiat spending(based on average data)"

def setupEnv():
  header = "transaction_type,bought coin symbol,bought coin amount, \
            bought coin unit price,sold coin symbol,sold coin amount, \
            sold coin unit price,total spending in fiat"
  with open(db_path, 'w') as f:
    f.write(header)
  with open(calc_path, 'w') as f:
    f.write(calc_path_header)

def saveBasicTradingInfo(type):
  symbol = input("Enter the bought cryptocurrency symbol(as mentioned in coinmarketcap): ")
  amount = input("Enter the amount of "+ symbol + " bought: ")
  price = input("Enter per unit price for "+ symbol + "(in SGD): ")
  total_spending = float(amount)*float(price)
  print("User bought ", amount, " units of ", symbol, " at unit price :" , price, "SGD")
  print("Total spending is: ", total_spending, "SGD")
  with open(db_path, "a") as f:
    data = "\n"+type+","+symbol+","+amount+","+price+","+","+","+"," + str(total_spending)
    f.write(data)
  updateBalanceSheet(type, symbol, amount, total_spending)
  return

def updateBalanceSheet(type, symbol_of_coin, amount_of_coin, total_fiat_spending):
  with open(calc_path, 'r') as f:
    lines = f.readlines()
  if len(lines) > 1:
    print("Number of entries: ", len(lines))
  symbols, total_amounts, prices, fiat_spendings = [], [], [], []
  for line in lines[1:]:
    symbol, total_amount, price, fiat_spending = line.split(",")
    total_amount = float(total_amount)
    price = float(price)
    fiat_spending = float(fiat_spending)
    symbols.append(symbol)
    total_amounts.append(total_amount)
    prices.append(price)
    fiat_spendings.append(fiat_spending)
  if (type=="buy"):
    index_of_symbol = False
    if symbol_of_coin in symbols:
      index_of_symbol = symbols.index(symbol_of_coin)
      total_amounts[index_of_symbol] = total_amounts[index_of_symbol] + float(amount_of_coin)
      fiat_spendings[index_of_symbol] = fiat_spendings[index_of_symbol] + float(total_fiat_spending)
      prices[index_of_symbol] = fiat_spendings[index_of_symbol]/total_amounts[index_of_symbol]
    else:
      symbols.append(symbol_of_coin)
      total_amounts.append(amount_of_coin)
      fiat_spendings.append(total_fiat_spending)
      prices.append(float(total_fiat_spending)/float(amount_of_coin))
  data = calc_path_header
  with open(calc_path, 'w') as f:
    for i, symbol in enumerate(symbols):
      data += "\n"+symbol+","+str(total_amounts[i])+","+ \
              str(prices[i])+","+str(fiat_spendings[i])
    f.write(data)
  return

def saveCryptoTradingInfo(type):
  "symbol, total amount holding, average per unit price, fiat spending(based on average data)"
  pass

def Main():
  args = docopt(__doc__, version='ProfitEstimation 1.0')
  print(args)
  setup = args["setup"]
  save = args["save"]
  basic = args["basic"]
  crypto = args["crypto"]
  type = args["--type"] if args["--type"] else "trade"
  if setup:
    setupEnv()
  elif save:
    if basic:
      saveBasicTradingInfo(type)
    elif crypto:
      saveCryptoTradingInfo(type)   
  return

if __name__=="__main__":
  Main()

