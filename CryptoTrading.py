#!/usr/bin/env python3
"""
CryptoTrading.

Usage:
  CryptoTrading profit_estimate <ids_as_a_string>


Options:
  <ids_as_a_string>         cryptocurrency ids to get info from coin
                            market cap API

"""
import openpyxl
from docopt import docopt
from CryptoAnalyze import cryptocurrencyMap, cryptocurrencyQuotes

import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


class ProfitEstimation(object):
  """This class provides essential information about a coin pair based on 
  price found in coin market cap -  this may not be same as different 
  exchanges - but the direction of trade should be easy to guess"""

  def __init__(self, coin_1, coin_2):
    self.coin_1_symbol = coin_1
    self.coin_1_price = -1
    self.coin_2_symbol = coin_2
    self.coin_2_price = -1
    blockPrint()
    cryptocurrencyMap()
    self.all_cryptocurrency_info = cryptocurrencyQuotes(50)
    enablePrint()
    self.getCurrentPrice()
    print(self.coin_1_symbol, " -> ", self.coin_1_price)
    print(self.coin_2_symbol, " -> ", self.coin_2_price)


  def getCurrentPrice(self):
    for cryptocurrency_info in self.all_cryptocurrency_info:
      if (self.coin_1_price == -1 or self.coin_2_price == -1 ):
        if (cryptocurrency_info["symbol"] == self.coin_1_symbol):
          self.coin_1_price = cryptocurrency_info["price"]
        if (cryptocurrency_info["symbol"] == self.coin_2_symbol):
          self.coin_2_price = cryptocurrency_info["price"]
      else:
        break
    return

def Main():
  args = docopt(__doc__, version='CryptoAnalyze 1.0')
  if (args["profit_estimate"]):
    coin_1 = args["<ids_as_a_string>"].split(",")[0]
    coin_2 = args["<ids_as_a_string>"].split(",")[1]
    pe = ProfitEstimation(coin_1, coin_2)
  return

if __name__ == "__main__":
  Main()
  