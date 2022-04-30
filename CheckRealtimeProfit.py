from cgitb import enable
from numpy import greater
from CheckBalance import checkBalance
from ReadStoredBalances import readStoredBalances
from Globals import *
from CoinMarketCapData import getCryptoCurrencyQuotes
from common_func import blockPrint, enablePrint

def checkRealtimeProfitLoss(symbol):
  blockPrint()
  total_amount_stored, price_stored, fiat_spending_stored, past_profit = checkBalance(symbol)
  enablePrint()
  price_current = getCurrentPrice(symbol)
  total_amount_stored = float(total_amount_stored)
  price_stored = float(price_stored)
  fiat_spending_stored = float(fiat_spending_stored)
  past_profit = float(past_profit)
  fiat_value_current = price_current * total_amount_stored
  if fiat_value_current > fiat_spending_stored:
    status_profit = True
  else:
    status_profit = False
  print("Summary:")
  print("Current Price per Unit of ", BLUE, symbol, BLACK, " is = ", price_current)
  print("Avg. Price per Unit of bought ", BLUE, symbol, BLACK, " is = ", price_stored)
  if status_profit:
    print("Profit = ", GREEN, fiat_value_current-fiat_spending_stored, BLACK)
  else:
    print("Loss = ", RED, fiat_spending_stored-fiat_value_current, BLACK)
  

  
def getCurrentPrice(symbol):
  coinmarketcap_coin_info = getCryptoCurrencyQuotes(100)
  price = 0.0
  for cryptocurrency_info in coinmarketcap_coin_info:
    if (cryptocurrency_info["symbol"] == symbol):
      price = cryptocurrency_info["price"]
      price = float(price)
      break
  else:
    print("No such coin in coin market cap. Please check spelling and try increasing coin count to retrieve info")
  return price



def checkAllRealtimeProfitLoss():
  coin_info = readStoredBalances()
  symbols, total_amounts, prices, fiat_spendings, past_profits = coin_info
  prices_current = getCurrentPrices(symbols)
  print("Summary:")
  for index, symbol in enumerate(symbols):
    blockPrint()
    total_amount_stored, price_stored, fiat_spending_stored, past_profit = checkBalance(symbol)
    enablePrint()
    price_current = float(prices_current[index])
    total_amount_stored = float(total_amount_stored)
    price_stored = float(price_stored)
    fiat_spending_stored = float(fiat_spending_stored)
    past_profit = float(past_profit)
    fiat_value_current = price_current * total_amount_stored
    if fiat_value_current > fiat_spending_stored:
      status_profit = True
    else:
      status_profit = False
    print("\nSymbol : ",BLUE_BOLD, symbol, BLACK)
    print("Current Price per Unit of ", BLUE, symbol, BLACK, " is = ", price_current)
    print("Avg. Price per Unit of bought ", BLUE, symbol, BLACK, " is = ", price_stored)
    if status_profit:
      print("Profit = ", GREEN, fiat_value_current-fiat_spending_stored, BLACK)
    else:
      print("Loss = ", RED, fiat_spending_stored-fiat_value_current, BLACK)
  print("\n")
  return


def getCurrentPrices(symbols):
  coinmarketcap_coin_info = getCryptoCurrencyQuotes(100)
  prices = []
  for symbol in symbols:
    price = 0.0
    for cryptocurrency_info in coinmarketcap_coin_info:
      if (cryptocurrency_info["symbol"] == symbol):
        price = cryptocurrency_info["price"]
        price = float(price)
        break
    else:
      print("No such coin in coin market cap. Please check spelling and try increasing coin count to retrieve info")
    prices.append(price)
  return prices