#!/usr/bin/env python3
"""
CryptoTrading.

Usage:
  CryptoTrading profit_estimate <ids_as_a_string> [--excel_file=<ef>]


Options:
  <ids_as_a_string>         cryptocurrency ids to get info from coin
                            market cap API
  
  --excel_file=<ef>         path to the excel file that contains CRO,ADA calculation
                            need to make it generalized later

"""


from numpy import save
from openpyxl import Workbook, load_workbook
from docopt import docopt
from CryptoAnalyze import getCryptoCurrencyQuotes
from ProfitEstimation import ProfitEstimation, profitEstimation
import os


def updateExcel(coin_1, coin_2, excel_file):
  pe = ProfitEstimation(coin_1, coin_2)
  workbook = load_workbook(excel_file)
  output = excel_file.replace(".xlsx", "_latest_datas.xlsx")
  if os.path.exists(output):
    os.remove(output)
    print(output, " is deleted")
  sheet = workbook.worksheets[1]
  sheet["G11"] = pe.coin_1_price
  sheet["G12"] = pe.coin_2_price
  workbook.save(output)
  print(output, " is created")
  return


def Main():
  args = docopt(__doc__, version='CryptoAnalyze 1.0')
  if (args["profit_estimate"]):
    coin_1 = args["<ids_as_a_string>"].split(",")[0]
    coin_2 = args["<ids_as_a_string>"].split(",")[1]
    if args["--excel_file"]:
      print("updateExcel")
      excel_file = args["--excel_file"] if args["--excel_file"]!="abc" else "/mnt/c/Users/shake/OneDrive/Desktop/coin market cap/cryptoInvestCalculator.xlsx"
      updateExcel(coin_1, coin_2, excel_file)
    else:
      print("profitEstimation")
      profitEstimation(coin_1, coin_2)
  return

if __name__ == "__main__":
  Main()
  