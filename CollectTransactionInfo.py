#!/usr/bin/env python3

from Globals import *


def collectBuyCoinInfo(coin_info):
  symbols, total_amounts, prices, fiat_spendings, past_profits = coin_info
  symbol = input("Enter the bought cryptocurrency symbol(as mentioned in coinmarketcap): "+GREEN_BOLD)
  if symbol in symbols:
      index = symbols.index(symbol)
      total_amount_stored = str(total_amounts[index])
      price_stored = str(prices[index])
      fiat_spending_stored = str(fiat_spendings[index])
      past_profit = str(past_profits[index])
      if past_profit.strip() == "":
        past_profit = "0"
      print(BLACK+ "Current balance of        "+GREEN+symbol+BLACK+" = "+total_amount_stored)
      print(BLACK+ "Current price per unit of "+GREEN+symbol+BLACK+" = "+price_stored)
      print(BLACK+ "Current fiat value of     "+GREEN+symbol+BLACK+" = "+fiat_spending_stored)
      print(BLACK+ "Past profit from trading  "+GREEN+symbol+BLACK+" = "+past_profit)
  else:
    print(BLACK+ "No existing balance available for " + GREEN + symbol + BLACK)
    past_profit = "0"
  amount = input("Enter the amount of "+GREEN+symbol+BLACK+" bought: "+BLACK_BOLD)
  price = input(BLACK+ "Enter per unit price for "+GREEN+symbol+BLACK+"(in SGD): "+BLACK_BOLD)
  total_spending = float(amount) * float(price)
  print(BLACK, "\nUser bought ", amount, " units of ", GREEN, symbol, BLACK, " at unit price :" , price, "SGD")
  print("Total spending is: ", RED, total_spending, "SGD", BLACK)
  return (symbol, amount, price, total_spending, past_profit)

def collectSellCoinInfo(coin_info):
  symbols, total_amounts, prices, fiat_spendings, past_profits = coin_info
  symbol = input("Enter the sold cryptocurrency symbol(as mentioned in coinmarketcap): "+ RED_BOLD)
  if symbol in symbols:
    index = symbols.index(symbol)
    total_amount_stored = str(total_amounts[index])
    price_stored = str(prices[index])
    fiat_spending_stored = str(fiat_spendings[index])
    past_profit = str(past_profits[index])
    if past_profit.strip() == "":
        past_profit = "0"
    print(BLACK+"Current balance of        "+RED+symbol+BLACK+" = "+total_amount_stored)
    print(BLACK+"Current price per unit of "+RED+symbol+BLACK+" = "+price_stored)
    print(BLACK+"Current fiat value of     "+RED+symbol+BLACK+" = "+fiat_spending_stored)
    print(BLACK+"Past profit from trading  "+RED+symbol+BLACK+" = "+past_profit)
  else:
    print("No existing balance available for " +RED+ symbol+BLACK)
    past_profit = "0"
  amount = input("Enter the amount of "+RED+symbol+BLACK+ " sold: "+BLACK_BOLD)
  while (float(amount)>float(total_amount_stored)):
    print(BLACK+"Please enter a valid amount that is lower or equal to existing balance of "+symbol+RED_BOLD)
    amount = input(BLACK+"Enter the amount of "+RED+symbol+BLACK+" sold: "+BLACK_BOLD)
  price = input(BLACK+"Enter per unit price for "+RED+symbol+BLACK+ "(in SGD): "+BLACK_BOLD)
  total_earning = float(amount)*float(price)
  print(BLACK, "\nUser sold ", amount, " units of ", RED, symbol, BLACK, " at unit price :" , price, "SGD")
  print("Total earning is: ", GREEN, total_earning, "SGD", BLACK)
  return (symbol, amount, price, total_earning, past_profit)

def collectTradeInfo(coin_info):
  symbol_sell, amount_sell, price_sell, total_earning_sell, past_profit_sell = collectSellCoinInfo(coin_info)
  symbol_buy, amount_buy, price_buy, total_spending_buy, past_profit_buy = collectBuyCoinInfo(coin_info)
  print("User traded ", amount_sell, " units of ", GREEN, symbol_sell, BLACK, " at unit price :" ,price_sell, "SGD",\
        "for ", amount_buy, " units of ", RED, symbol_buy, BLACK, " at unit price :", price_buy, "SGD",)
  print("Total spending is: ", RED, total_earning_sell, BLACK, "SGD in today's market value")
  print("Total value after buy is: ", GREEN, total_spending_buy, BLACK, "SGD in today's market value")
  sell_coin = (symbol_sell, amount_sell, price_sell, total_earning_sell)
  buy_coin = (symbol_buy, amount_buy, price_buy, total_spending_buy)
  return (sell_coin, buy_coin)
