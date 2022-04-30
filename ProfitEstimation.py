#!/usr/bin/env python3
"""
ProfitEstimation.

Usage:
  ProfitEstimation save [--type=(buy|trade|sell)]
  ProfitEstimation balance [--symbol=<symbol>]
  ProfitEstimation profit [--symbol=<symbol>]
  ProfitEstimation setup


Options:
  setup           run this command only first time for setup
  save            indicates some info will be saved for future use
  balance         check the balance of a particular coin

  buy             user bought cryptocurrency with fiat money
  sell            user sold cryptocurrency for fiat money
  trade           user traded one cryptocurrency for another

"""

from tabnanny import check
from docopt import docopt
from JsonExtract import *
from common_func import *
from Globals import *
from SaveTradingInfo import saveTradingInfo
from CheckBalance import checkBalance, checkAllBalance
from CheckRealtimeProfit import checkRealtimeProfitLoss, checkAllRealtimeProfitLoss
from SetupEnv import setupEnv



def Main():
  args = docopt(__doc__, version='ProfitEstimation 1.0')
  setup = args["setup"]
  save = args["save"]
  balance = args["balance"]
  profit = args["profit"]
  type = args["--type"] if args["--type"] else "trade"
  if setup:
    setupEnv()
  elif save:
    saveTradingInfo(type)
  elif balance:
    symbol = args["--symbol"]
    if symbol:
      checkBalance(symbol)
    else:
      checkAllBalance()
  elif profit:
    symbol = args["--symbol"]
    if symbol:
      checkRealtimeProfitLoss(symbol)
    else:
      checkAllRealtimeProfitLoss()
  return

if __name__=="__main__":
  Main()

