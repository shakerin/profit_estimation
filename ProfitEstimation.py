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

db_transaction_path = "./transaction_sheet.csv"
db_transaction_header = "transaction_type,bought coin symbol,bought coin amount," + \
                        "bought coin unit price,sold coin symbol,sold coin amount," + \
                        "sold coin unit price,total spending in fiat"

db_balances_path = "./balance_sheets.csv"
db_balances_path_header = "symbol, total amount holding, average per unit price, fiat spending(based on average data)"

def setupEnv():
  with open(db_transaction_path, 'w') as f:
    f.write(db_transaction_header)
  with open(db_balances_path, 'w') as f:
    f.write(db_balances_path_header)

def saveBasicTradingInfo(type):
  symbols, total_amounts, prices, fiat_spendings = readStoredBalances()
  if (type=='buy'):
    symbol = input("Enter the bought cryptocurrency symbol(as mentioned in coinmarketcap): ")
    if symbol in symbols:
      index = symbols.index(symbol)
      total_amount_stored = str(total_amounts[index])
      price_stored = str(prices[index])
      fiat_spending_stored = str(fiat_spendings[index])
      print("Current balance of "+symbol+" = "+total_amount_stored)
      print("Current price per unit of "+symbol+" = "+price_stored)
      print("Current fiat value of "+symbol+" = "+fiat_spending_stored)
    else:
      print("No existing balance available for " + symbol)
    amount = input("Enter the amount of "+ symbol + " bought: ")
    price = input("Enter per unit price for "+ symbol + "(in SGD): ")
    total_spending = float(amount) * float(price)
    print("User bought ", amount, " units of ", symbol, " at unit price :" , price, "SGD")
    print("Total spending is: ", total_spending, "SGD")
    updateTransactionSheetAfterBuy(symbol, amount, price, total_spending)
    updateBalanceSheetAfterBuy(symbol, amount, total_spending)

  elif (type=='sell'):
    symbol = input("Enter the sold cryptocurrency symbol(as mentioned in coinmarketcap): ")
    if symbol in symbols:
      index = symbols.index(symbol)
      total_amount_stored = str(total_amounts[index])
      price_stored = str(prices[index])
      fiat_spending_stored = str(fiat_spendings[index])
      print("Current balance of "+symbol+" = "+total_amount_stored)
      print("Current price per unit of "+symbol+" = "+price_stored)
      print("Current fiat value of "+symbol+" = "+fiat_spending_stored)
    else:
      print("No existing balance available for " + symbol)
    amount = input("Enter the amount of "+ symbol + " sold: ")
    while (float(amount)>float(total_amount_stored)):
      print("Please enter a valid amount that is lower or equal to exisitng balance of "+symbol)
      amount = input("Enter the amount of "+ symbol + " sold: ")
    price = input("Enter per unit price for "+ symbol + "(in SGD): ")
    total_earning = float(amount)*float(price)
    print("User sold ", amount, " units of ", symbol, " at unit price :" , price, "SGD")
    print("Total earning is: ", total_earning, "SGD")
    updateTransactionSheetAfterSell(symbol, amount, price, total_earning)
    updateBalanceSheetAfterSell(symbol, amount, total_earning)

  elif (type=='trade'):
    symbol_sell = input("Enter the sold cryptocurrency symbol(as mentioned in coinmarketcap): ")
    if symbol_sell in symbols:
      index = symbols.index(symbol_sell)
      total_amount_stored = str(total_amounts[index])
      price_stored = str(prices[index])
      fiat_spending_stored = str(fiat_spendings[index])
      print("Current balance of "+symbol_sell+" = "+total_amount_stored)
      print("Current price per unit of "+symbol_sell+" = "+price_stored)
      print("Current fiat value of "+symbol_sell+" = "+fiat_spending_stored)
    else:
      print("No existing balance available for " + symbol_sell)
    amount_sell = input("Enter the amount of "+ symbol_sell + " sold: ")
    while (float(amount_sell)>float(total_amount_stored)):
      print("Please enter a valid amount that is lower or equal to exisitng balance of "+symbol_sell)
      print(amount_sell, total_amount_stored)
      amount_sell = input("Enter the amount of "+ symbol_sell + " sold: ")
    price_sell = input("Enter per unit price for "+ symbol_sell + "(in SGD): ")
    total_earning_sell = float(amount_sell)*float(price_sell)
    symbol_buy = input("Enter the bought cryptocurrency symbol(as mentioned in coinmarketcap): ")
    if symbol_buy in symbols:
      index = symbols.index(symbol_buy)
      total_amount_stored = str(total_amounts[index])
      price_stored = str(prices[index])
      fiat_spending_stored = str(fiat_spendings[index])
      print("Current balance of "+symbol_buy+" = "+total_amount_stored)
      print("Current price per unit of "+symbol_buy+" = "+price_stored)
      print("Current fiat value of "+symbol_buy+" = "+fiat_spending_stored)
    else:
      print("No existing balance available for " + symbol_buy)
    amount_buy = input("Enter the amount of "+ symbol_buy + " bought: ")
    price_buy = input("Enter per unit price for "+ symbol_buy + "(in SGD): ")
    total_earning_buy = float(amount_buy)*float(price_buy)
    print("User traded ", amount_sell, " units of ", symbol_sell, " at unit price :" , price_sell, "SGD",\
          "for ", amount_buy, " units of ", symbol_buy, " at unit price :", price_buy, "SGD")
    print("Total spending is: ", total_earning_sell, "SGD in today's market value")
    print("Total value after buy is: ", total_earning_buy, "SGD in today's market value")
    coin_sell = (symbol_buy, amount_buy, price_buy, total_earning_buy)
    coin_buy = (symbol_sell, amount_sell, price_sell, total_earning_sell)
    updateTransactionSheetAfterTrade(coin_sell, coin_buy)
    updateBalanceSheetAfterTrade(coin_sell, coin_buy)
  return

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
      data = "\n"+"Trade,"+symbol_buy+","+amount_buy+","+price_buy+","+symbol_sell+","+amount_sell+","+price_sell+","+ str(total_spending_sell)
      f.write(data)
  return


def readStoredBalances():
  with open(db_balances_path, 'r') as f:
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
  return (symbols, total_amounts, prices, fiat_spendings)

def updateBalanceSheetAfterBuy(symbol_of_coin, amount_of_coin, total_fiat_spending):
  symbols, total_amounts, prices, fiat_spendings = readStoredBalances()
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
  storeNewBalanceData(symbols, total_amounts, prices, fiat_spendings)
  return


def updateBalanceSheetAfterSell(symbol_of_coin, amount_of_coin, total_fiat_earning):
  symbols, total_amounts, prices, fiat_spendings = readStoredBalances()
  index_of_symbol = symbols.index(symbol_of_coin)
  
  total_amounts[index_of_symbol] = total_amounts[index_of_symbol] - float(amount_of_coin)
  fiat_spendings[index_of_symbol] = fiat_spendings[index_of_symbol] - float(total_fiat_earning)
  if (total_amounts[index_of_symbol]) != 0:
    prices[index_of_symbol] = fiat_spendings[index_of_symbol]/total_amounts[index_of_symbol]
  else:
    prices[index_of_symbol] = 0.0
  storeNewBalanceData(symbols, total_amounts, prices, fiat_spendings)
  return

def updateBalanceSheetAfterTrade(coin_buy, coin_sell):
  symbol_sell, amount_sell, price_sell, total_spending_sell = coin_sell
  symbol_buy, amount_buy, price_buy, total_spending_buy = coin_buy
  updateBalanceSheetAfterSell(symbol_sell, amount_sell, total_spending_sell)
  updateBalanceSheetAfterBuy(symbol_buy, amount_buy, total_spending_sell)
  return

def saveCryptoTradingInfo(type):
  "symbol, total amount holding, average per unit price, fiat spending(based on average data)"
  pass

def storeNewBalanceData(symbols, total_amounts, prices, fiat_spendings):
  data = db_balances_path_header
  with open(db_balances_path, 'w') as f:
    for i, symbol in enumerate(symbols):
      data += "\n"+symbol+","+str(total_amounts[i])+","+ \
              str(prices[i])+","+str(fiat_spendings[i])
    f.write(data)
  return



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

