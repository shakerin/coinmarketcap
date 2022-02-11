#!/usr/bin/env python3
"""
CryptoAnalyze.

Usage:
  CryptoAnalyze basic
  CryptoAnalyze exchange [--map|--info]
"""
from inspect import Parameter
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from docopt import docopt



def getSession():
  """Setting up session for making api call to coin market cap"""
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '77c61b7b-0cde-4775-9fa4-1dc7609334d7',
  }
  session = Session()
  session.headers.update(headers)
  return session

def callAPI(url, session, parameters, output_file):
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    with open(output_file, 'w') as f:
      json.dump(data, f, indent=4)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)



def cryptoListing():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  session = getSession()
  parameters = {
    'start':'1',
    'limit':'100',
    'convert':'USD'
  }
  output_file = "cryptocurrency.listings.latest.json"
  callAPI(url, session, parameters, output_file)


def exchangeMap():
  url = "https://pro-api.coinmarketcap.com/v1/exchange/map"
  session = getSession()
  parameters = {
    'start':'1',
    'limit':'200',
    'sort':'volume_24h'
  }
  output_file = "exchange.map.json"
  callAPI(url, session, parameters, output_file)


def exchangeInfo():
  url = "https://pro-api.coinmarketcap.com/v1/exchange/info"
  session = getSession()
  parameters = {
    'id':'270,294,513,524,1507,521,538,633,391,407,102,549,311,955,1149,302'
  }
  output_file = "exchange.info.json"
  callAPI(url, session, parameters, output_file)




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
  
  
  return




if __name__ == "__main__":
  Main()