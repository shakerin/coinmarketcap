from tkinter import E
from numpy import save
from openpyxl import Workbook, load_workbook
from docopt import docopt
from common_func import *
from CryptoAnalyze import getCryptoCurrencyQuotes

class ProfitEstimation(object):
  """This class provides essential information about a coin pair based on 
  price found in coin market cap -  this may not be same as different 
  exchanges - but the direction of trade should be easy to guess"""

  def __init__(self, coin_1, coin_2):
    self.coin_1_symbol = coin_1
    self.coin_1_price = -1
    self.coin_2_symbol = coin_2
    self.coin_2_price = -1
    self.all_cryptocurrency_info = getCryptoCurrencyQuotes(50)
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

def profitEstimation(coin_1, coin_2):
  pe = ProfitEstimation(coin_1, coin_2)
  return