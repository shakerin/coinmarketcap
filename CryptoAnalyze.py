#!/usr/bin/env python3
"""
CryptoAnalyze.

Usage:
  CryptoAnalyze basic
  CryptoAnalyze exchange map
  CryptoAnalyze exchange info --no=<no>
  CryptoAnalyze exchange compare <exchange1> <exchange2>
  CryptoAnalyze cryptocurrency [--categories|--map]
  CryptoAnalyze cryptocurrency (info|quotes) --no=<no>


Options:
  --no=<no>         Number of exchanges to get information about.
  --categories      Get information based on Cryptocurrenct categories.

"""
from inspect import Parameter
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from docopt import docopt
from JsonExtract import *



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




def exchangeInfo(no_of_exchanges):
  url = "https://pro-api.coinmarketcap.com/v1/exchange/info"
  json_file_path = "https://pro-api.coinmarketcap.com/v1/exchange/map".split(".com")[1].replace("/",".")[1:]+".json"
  all_ids, all_ids_one_string = getTopExchangeIds(json_file_path, no_of_exchanges)
  all_exchanges, all_exchanges_one_string = getTopExchangeNames(json_file_path, no_of_exchanges)
  parameters = {
    'id':all_ids_one_string
  }
  ca = CryptoAnalyze(url, parameters)
  ca.getResult()
  for i,exchange in enumerate(all_exchanges):
    print(str(i+1), ". ", exchange)
    print("======================================")
    exchange_info = getExchangeInfo(ca.output_file, all_ids[i])
    print("Description:")
    #print(" ", exchange_info["description"])
    print("Id                   : ", str(all_ids[i]))
    print("Website              : ", exchange_info["website"])
    print("Date Launched        : ", exchange_info["date_launched"])
    print("Spot Volume (in US$) : ", exchange_info["spot_volume_usd"])
    print("Weekly Visits        : ", exchange_info["weekly_visits"])
    print("Maker Fee            : ", exchange_info["maker_fee"])
    print("Taker Fee            : ", exchange_info["taker_fee"])
    print("======================================")
  return





def compareExchanges(exchange1_id, exchange2_id):
  url = "https://pro-api.coinmarketcap.com/v1/exchange/info"
  parameters = "n/a"
  ca = CryptoAnalyze(url, parameters)
  exchange1_info = getExchangeInfo(ca.output_file, exchange1_id)
  exchange2_info = getExchangeInfo(ca.output_file, exchange2_id)
  print("Comparison between," , exchange1_info["name"],  ",", exchange2_info["name"])
  print("Date Launched," , exchange1_info["date_launched"], ",", exchange2_info["date_launched"])
  print("Spot Volume (in US$)," , exchange1_info["spot_volume_usd"], ",", exchange2_info["spot_volume_usd"])
  print("Weekly Visits," , exchange1_info["weekly_visits"], ",", exchange2_info["weekly_visits"])



def cryptocurrencyMap():
  url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
  parameters = {
    'start':'1',
    'limit':'5000',
    'sort':'cmc_rank',
  }
  CryptoAnalyze(url, parameters).getResult()




def cryptocurrencyCategories():
  url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories"
  parameters = {
    'start':'1',
    'limit':'200'
  }
  CryptoAnalyze(url, parameters).getResult()



def cryptocurrencyInfo(no_of_cryptocurrencies):
  url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/info"
  json_file_path = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map".split(".com")[1].replace("/",".")[1:]+".json"
  all_ids, all_ids_one_string = getTopCryptocurrencyIds(json_file_path, no_of_cryptocurrencies)
  all_cryptocurrencies, all_cryptocurrencies_one_string = getTopCryptocurrencyNames(json_file_path, no_of_cryptocurrencies)
  parameters = {
    'id':all_ids_one_string
  }
  ca = CryptoAnalyze(url, parameters)
  ca.getResult()
  for i,cryptocurrency in enumerate(all_cryptocurrencies):
    print(str(i+1), ". ", cryptocurrency)
    print("======================================")
    cryptocurrency_info = getCryptocurrencyInfo(ca.output_file, all_ids[i])
    print("Description:")
    #print(" ", cryptocurrency_info["description"])
    print("Id                   : ", str(all_ids[i]))
    print("Name                 : ", cryptocurrency_info["name"])
    print("Symbol               : ", cryptocurrency_info["symbol"])
    print("Category             : ", cryptocurrency_info["category"])
    print("Description          : ", cryptocurrency_info["description"])
    print("Platform             : ", cryptocurrency_info["platform"])
    print("Date added           : ", cryptocurrency_info["date_added"])
    print("Date launched        : ", cryptocurrency_info["date_launched"])
    print("Circulating Supply   : ", cryptocurrency_info["self_reported_circulating_supply"])
    print("Market Cap           : ", cryptocurrency_info["self_reported_market_cap"])
    print("Contract Addresses:")
    print("--------------------------------------")
    for i, platform in enumerate(cryptocurrency_info["contract_address"]):
      print("  ", str(i+1), ") Platform Name    : ", platform["platform"]["name"])
      print("    ",         ") Platform Id      : ", str(platform["platform"]["coin"]["id"]))
      print("    ",         ") Contract Address : ", platform["contract_address"])
    print("======================================")
  return


def cryptocurrencyQuotes(no_of_exchanges):
  url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
  json_file_path = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map".split(".com")[1].replace("/",".")[1:]+".json"
  all_ids, all_ids_one_string = getTopCryptocurrencyIds(json_file_path, no_of_exchanges)
  all_cryptocurrencies, all_cryptocurrencies_one_string = getTopCryptocurrencyNames(json_file_path, no_of_exchanges)
  parameters = {
    'id':all_ids_one_string,
    'convert' : "SGD"
  }
  ca = CryptoAnalyze(url, parameters)
  ca.getResult()
  cryptocurrency_info_list = []
  for i,cryptocurrency in enumerate(all_cryptocurrencies):
    cryptocurrency_info = getCryptocurrencyQuotes(ca.output_file, all_ids[i])
    cryptocurrency_info_list.append(cryptocurrency_info)
    print(str(i+1), ". ", cryptocurrency)
    print("======================================")
    print("Quotes:")
    print("Id                   : ", str(all_ids[i]))
    print("Name                 : ", cryptocurrency_info["name"])
    print("Symbol               : ", cryptocurrency_info["symbol"])
    print("Is Fiat?             : ", cryptocurrency_info["is_fiat"])
    print("Is Active?           : ", cryptocurrency_info["is_active"])
    print("Last Updated         : ", cryptocurrency_info["last_updated"])
    print("Price                : ", cryptocurrency_info["price"])
    print("Volume 24h           : ", cryptocurrency_info["volume_24h"])
    print("Market Cap           : ", cryptocurrency_info["market_cap"])
    print("Fully diluted M.Cap. : ", cryptocurrency_info["fully_diluted_market_cap"])
    print("======================================")
  return cryptocurrency_info_list



def Main():
  args = docopt(__doc__, version='CryptoAnalyze 1.0')
  if args['basic']:
    print("Read first 100 cryptocurrencies")
    cryptoListing()
  elif args['exchange']:
    if args["map"]:
      print("Read first 200 exchanges and sort by 24h volume")
      exchangeMap()
    elif args["info"]:
      print("Read top ", args["--no"], " exchange info")
      exchangeInfo(int(args["--no"]))
    elif args["compare"]:
      compareExchanges(args["<exchange1>"], args["<exchange2>"])
  elif args['cryptocurrency']:
    if args["info"]:
      print("Read top ", args["--no"], " cryptocurrency info")
      cryptocurrencyInfo(int(args["--no"]))
    elif args["quotes"]:
      print("Read top ", args["--no"], " cryptocurrency quotes")
      cryptocurrencyQuotes(int(args["--no"]))
    else:
      if args['--categories']:
        print("Read first 200 cryptocurrencies based on category")
        cryptocurrencyCategories()
      elif args['--map']:
        print("Read cryptocurrenct map for 5000 coins sorted by cmc_rank")
        cryptocurrencyMap()
  return




if __name__ == "__main__":
  Main()