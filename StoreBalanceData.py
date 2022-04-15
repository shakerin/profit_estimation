#!/usr/bin/env python3
from Globals import *

def storeNewBalanceData(symbols, total_amounts, prices, fiat_spendings, past_profits):
  data = db_balances_path_header
  with open(db_balances_path, 'w') as f:
    for i, symbol in enumerate(symbols):
      data += "\n"+symbol+","+str(total_amounts[i])+","+ \
              str(prices[i])+","+str(fiat_spendings[i])+","+ \
              str(past_profits[i]).strip()
    f.write(data)
  return

