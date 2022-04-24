#!/usr/bin/env python3
from Globals import *
from ReadStoredBalances import readStoredBalances

from CollectTransactionInfo import(
  collectBuyCoinInfo,
  collectSellCoinInfo,
  collectTradeInfo
)

from UpdateTransactionSheet import (
  updateTransactionSheetAfterBuy,
  updateTransactionSheetAfterSell,
  updateTransactionSheetAfterTrade
)
from UpdateBalanceSheet import(
  updateBalanceSheetAfterBuy,
  updateBalanceSheetAfterSell,
  updateBalanceSheetAfterTrade
)



def saveTradingInfo(type):
  coin_info = readStoredBalances()
  if (type=='buy'):
    symbol, amount, price, total_spending, past_profit = collectBuyCoinInfo(coin_info)
    updateTransactionSheetAfterBuy(symbol, amount, price, total_spending)
    updateBalanceSheetAfterBuy(symbol, amount, total_spending)

  elif (type=='sell'):
    symbol, amount, price, total_earning, past_profit = collectSellCoinInfo(coin_info)
    updateTransactionSheetAfterSell(symbol, amount, price, total_earning)
    updateBalanceSheetAfterSell(symbol, amount, total_earning)

  elif (type=='trade'):
    coin_sell, coin_buy = collectTradeInfo(coin_info)
    updateTransactionSheetAfterTrade(coin_sell, coin_buy)
    updateBalanceSheetAfterTrade(coin_sell, coin_buy)
  return




