#!/usr/bin/env python3
from Globals import *
from StoreBalanceData import storeNewBalanceData
from ReadStoredBalances import readStoredBalances

def updateBalanceSheetAfterBuy(symbol_of_coin, amount_of_coin, total_fiat_spending):
  symbols, total_amounts, prices, fiat_spendings, past_profits = readStoredBalances()
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
    past_profits.append("0")
  storeNewBalanceData(symbols, total_amounts, prices, fiat_spendings, past_profits)
  return


def updateBalanceSheetAfterSell(symbol_of_coin, amount_of_coin, total_fiat_earning):
  symbols, total_amounts, prices, fiat_spendings, past_profits = readStoredBalances()
  index_of_symbol = symbols.index(symbol_of_coin)
  
  total_amounts[index_of_symbol] = total_amounts[index_of_symbol] - float(amount_of_coin)
  fiat_spendings[index_of_symbol] = fiat_spendings[index_of_symbol] - float(total_fiat_earning)
  if total_amounts[index_of_symbol] == 0:
    past_profits[index_of_symbol] = (float(past_profits[index_of_symbol]) + -1.0*fiat_spendings[index_of_symbol])
    fiat_spendings[index_of_symbol] = 0
  if (total_amounts[index_of_symbol]) != 0:
    prices[index_of_symbol] = fiat_spendings[index_of_symbol]/total_amounts[index_of_symbol]
  else:
    prices[index_of_symbol] = 0.0
  storeNewBalanceData(symbols, total_amounts, prices, fiat_spendings, past_profits)
  return

def updateBalanceSheetAfterTrade(coin_sell, coin_buy):
  symbol_sell, amount_sell, price_sell, total_spending_sell = coin_sell
  symbol_buy, amount_buy, price_buy, total_spending_buy = coin_buy
  updateBalanceSheetAfterSell(symbol_sell, amount_sell, total_spending_sell)
  updateBalanceSheetAfterBuy(symbol_buy, amount_buy, total_spending_sell)
  return