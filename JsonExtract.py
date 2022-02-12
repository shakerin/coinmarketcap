#!/usr/bin/env python3
import json

def showExchangeNames(json_file):
  with open(json_file, 'r') as f:
    data_as_json = f.read()
  data_as_dict = json.loads(data_as_json)
  exchange_data_as_list = data_as_dict["data"]
  for i, exchange in enumerate(exchange_data_as_list):
    print(str(i+1), ") ", exchange["name"]," (", exchange["id"], ") ", exchange["first_historical_data"])
  
def getTopExchangeNames(json_file, no):
  with open(json_file, 'r') as f:
    data_as_json = f.read()
    data_as_dict = json.loads(data_as_json)
    exchange_data_as_list = data_as_dict["data"]
    exchange_names = []
    for exchange in exchange_data_as_list[0:no]:
      exchange_names.append(exchange["name"])
  exchange_names_one_string = ",".join(exchange_names)
  return (exchange_names, exchange_names_one_string)


def getTopExchangeIds(json_file, no):
  with open(json_file, 'r') as f:
    data_as_json = f.read()
    data_as_dict = json.loads(data_as_json)
    exchange_data_as_list = data_as_dict["data"]
    exchange_ids = []
    for exchange in exchange_data_as_list[0:no]:
      exchange_ids.append(str(exchange["id"]))
  exchange_ids_one_string = ",".join(exchange_ids)
  return (exchange_ids, exchange_ids_one_string)



def Main():
  json_file = "v1.exchange.map.json"
  #showExchangeNames(json_file)
  #ex_names = getTopExchangeNames(json_file, 15)
  #print(ex_names)
  ex_ids = getTopExchangeIds(json_file, 15)
  print(ex_ids)

if __name__ == "__main__":
  Main()