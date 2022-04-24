#!/usr/bin/env python3
"""
ProfitEstimation.

Usage:
  ProfitEstimation save [--type=(buy|trade|sell)]
  ProfitEstimation balance <symbol>
  ProfitEstimation profit <symbol>
  ProfitEstimation setup


Options:
  setup           run this command only first time for setup
  save            indicates some info will be saved for future use
  balance         check the balance of a particular coin

  buy             user bought cryptocurrency with fiat money
  sell            user sold cryptocurrency for fiat money
  trade           user traded one cryptocurrency for another

"""

from docopt import docopt
from JsonExtract import *
from common_func import *
from Globals import *
from SaveTradingInfo import saveTradingInfo
from CheckBalance import checkBalance
from CheckRealtimeProfit import checkRealtimeProfitLoss
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
    symbol = args["<symbol>"]
    checkBalance(symbol)
  elif profit:
    symbol = args["<symbol>"]
    checkRealtimeProfitLoss(symbol)
  return

if __name__=="__main__":
  Main()

