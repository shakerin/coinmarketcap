#!/usr/bin/env python3
"""
CryptoAnalyze.

Usage:
  CryptoAnalyze basic
  CryptoAnalyze exchange [--map|--info]
  CryptoAnalyze cryptocurrency [--categories]
"""
from inspect import Parameter
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from docopt import docopt

from JsonExtract import getTopExchangeIds



class CryptoAnalyze():
  def __init__(self, url, parameters):
    self.url = url
    self.parameters = parameters
    self.output_file = self.url.split(".com")[1].replace("/",".")[1:]+".json"
  
  def getResult(self):
    self.setupSession()
    self.callAPI()

  def setupSession(self):
    """Setting up session for making api call to coin market cap"""
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '77c61b7b-0cde-4775-9fa4-1dc7609334d7',
    }
    self.session = Session()
    self.session.headers.update(headers)
    return 

  def callAPI(self):
    try:
      response = self.session.get(self.url, params=self.parameters)
      data = json.loads(response.text)
      with open(self.output_file, 'w') as f:
        json.dump(data, f, indent=4)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)





def cryptoListing():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'100',
    'convert':'USD'
  }
  CryptoAnalyze(url, parameters).getResult()

  


def exchangeMap():
  url = "https://pro-api.coinmarketcap.com/v1/exchange/map"
  parameters = {
    'start':'1',
    'limit':'200',
    'sort':'volume_24h'
  }
  CryptoAnalyze(url, parameters).getResult()


def exchangeInfo():
  url = "https://pro-api.coinmarketcap.com/v1/exchange/info"
  all_ids, all_ids_one_string = getTopExchangeIds("https://pro-api.coinmarketcap.com/v1/exchange/map".split(".com")[1].replace("/",".")[1:]+".json", 15)
  parameters = {
    'id':all_ids_one_string
  }
  CryptoAnalyze(url, parameters).getResult()



def cryptocurrencyCategories():
  url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories"
  parameters = {
    'start':'1',
    'limit':'200'
  }
  CryptoAnalyze(url, parameters).getResult()



def Main():
  args = docopt(__doc__, version='CryptoAnalyze 1.0')
  if args['basic']:
    print("Read first 100 cryptocurrencies")
    cryptoListing()
  elif args['exchange']:
    if args["--map"]:
      print("Read first 200 exchanges and sort by 24h volume")
      exchangeMap()
    elif args["--info"]:
      print("Read top exchange info")
      exchangeInfo()
  elif args['cryptocurrency']:
    if args['--categories']:
      print("Read first 200 cryptocurrencies based on category")
      cryptocurrencyCategories()
  
  
  return




if __name__ == "__main__":
  Main()