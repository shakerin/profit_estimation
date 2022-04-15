#!/usr/bin/env python3
from Globals import *

def readStoredBalances():
  with open(db_balances_path, 'r') as f:
    lines = f.readlines()
  if len(lines) <= 1:
    print("Number of entries: ", len(lines))
  symbols, total_amounts, prices, fiat_spendings, past_profits = [], [], [], [], []
  for line in lines[1:]:
    symbol, total_amount, price, fiat_spending, past_profit = line.split(",")
    if past_profit.strip() == "":
      past_profit = "0"
    total_amount = float(total_amount)
    price = float(price)
    fiat_spending = float(fiat_spending)
    symbols.append(symbol)
    total_amounts.append(total_amount)
    prices.append(price)
    fiat_spendings.append(fiat_spending)
    past_profits.append(past_profit)

  return (symbols, total_amounts, prices, fiat_spendings, past_profits)