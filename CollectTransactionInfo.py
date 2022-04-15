#!/usr/bin/env python3

def collectBuyCoinInfo(coin_info):
  symbols, total_amounts, prices, fiat_spendings, past_profits = coin_info
  symbol = input("Enter the bought cryptocurrency symbol(as mentioned in coinmarketcap): ")
  if symbol in symbols:
      index = symbols.index(symbol)
      total_amount_stored = str(total_amounts[index])
      price_stored = str(prices[index])
      fiat_spending_stored = str(fiat_spendings[index])
      past_profit = str(past_profits[index])
      if past_profit.strip() == "":
        past_profit = "0"
      print("Current balance of        "+symbol+" = "+total_amount_stored)
      print("Current price per unit of "+symbol+" = "+price_stored)
      print("Current fiat value of     "+symbol+" = "+fiat_spending_stored)
      print("Past profit from trading  "+symbol+" = "+past_profit)
  else:
    print("No existing balance available for " + symbol)
    past_profit = "0"
  amount = input("Enter the amount of "+ symbol + " bought: ")
  price = input("Enter per unit price for "+ symbol + "(in SGD): ")
  total_spending = float(amount) * float(price)
  print("User bought ", amount, " units of ", symbol, " at unit price :" , price, "SGD")
  print("Total spending is: ", total_spending, "SGD")
  return (symbol, amount, price, total_spending, past_profit)

def collectSellCoinInfo(coin_info):
  symbols, total_amounts, prices, fiat_spendings, past_profits = coin_info
  symbol = input("Enter the sold cryptocurrency symbol(as mentioned in coinmarketcap): ")
  if symbol in symbols:
    index = symbols.index(symbol)
    total_amount_stored = str(total_amounts[index])
    price_stored = str(prices[index])
    fiat_spending_stored = str(fiat_spendings[index])
    past_profit = str(past_profits[index])
    if past_profit.strip() == "":
        past_profit = "0"
    print("Current balance of        "+symbol+" = "+total_amount_stored)
    print("Current price per unit of "+symbol+" = "+price_stored)
    print("Current fiat value of     "+symbol+" = "+fiat_spending_stored)
    print("Past profit from trading  "+symbol+" = "+past_profit)
  else:
    print("No existing balance available for " + symbol)
    past_profit = "0"
  amount = input("Enter the amount of "+ symbol + " sold: ")
  while (float(amount)>float(total_amount_stored)):
    print("Please enter a valid amount that is lower or equal to exisitng balance of "+symbol)
    amount = input("Enter the amount of "+ symbol + " sold: ")
  price = input("Enter per unit price for "+ symbol + "(in SGD): ")
  total_earning = float(amount)*float(price)
  print("User sold ", amount, " units of ", symbol, " at unit price :" , price, "SGD")
  print("Total earning is: ", total_earning, "SGD")
  return (symbol, amount, price, total_earning, past_profit)

def collectTradeInfo(coin_info):
  symbol_sell, amount_sell, price_sell, total_earning_sell, past_profit_sell = collectSellCoinInfo(coin_info)
  symbol_buy, amount_buy, price_buy, total_spending_buy, past_profit_buy = collectBuyCoinInfo(coin_info)
  print("User traded ", amount_sell, " units of ", symbol_sell, " at unit price :" , price_sell, "SGD",\
        "for ", amount_buy, " units of ", symbol_buy, " at unit price :", price_buy, "SGD")
  print("Total spending is: ", total_earning_sell, "SGD in today's market value")
  print("Total value after buy is: ", total_spending_buy, "SGD in today's market value")
  sell_coin = (symbol_sell, amount_sell, price_sell, total_earning_sell)
  buy_coin = (symbol_buy, amount_buy, price_buy, total_spending_buy)
  return (sell_coin, buy_coin)
