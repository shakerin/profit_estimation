from ReadStoredBalances import readStoredBalances
from Globals import *

def checkBalance(symbol):
  coin_info = readStoredBalances()
  symbols, total_amounts, prices, fiat_spendings, past_profits = coin_info
  if symbol in symbols:
    index = symbols.index(symbol)
    total_amount_stored = str(total_amounts[index])
    price_stored = str(prices[index])
    fiat_spending_stored = str(fiat_spendings[index])
    past_profit = str(past_profits[index]).strip()
    if past_profit == "":
        past_profit = "0"
    print("\n")
    print("Balance           = "+GREEN_BOLD+total_amount_stored+BLACK)
    print("PPU               = "+price_stored)
    print("Fiat Value        = "+GREEN_BOLD+fiat_spending_stored+BLACK)
    print("Previous Balance  = "+past_profit)
  else:
    print("\n")
    print("No existing balance available for " + BLUE+symbol+BLACK)
  print("\n")
  return (total_amount_stored, price_stored, fiat_spending_stored, past_profit)


def checkAllBalance():
  coin_info = readStoredBalances()
  symbols, total_amounts, prices, fiat_spendings, past_profits = coin_info
  for index,symbol in enumerate(symbols):
    total_amount_stored = str(total_amounts[index])
    price_stored = str(prices[index])
    fiat_spending_stored = str(fiat_spendings[index])
    past_profit = str(past_profits[index]).strip()
    if past_profit == "":
        past_profit = "0"
    print("\n")
    print("Symbol : "+BLUE_BOLD+symbol+BLACK)
    print("--------------------")
    print("Balance           = "+GREEN_BOLD+total_amount_stored+BLACK)
    print("PPU               = "+price_stored)
    print("Fiat Value        = "+GREEN_BOLD+fiat_spending_stored+BLACK)
    print("Previous Balance  = "+past_profit)
  print("\n")
  return


