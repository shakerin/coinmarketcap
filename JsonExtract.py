#!/usr/bin/env python3
import json

def showExchangeNames(json_file):
  """This method just prints all exchanges names found
  
  returns nothing
  """
  crypto_json_extract_obj = CryptoJsonExtract(json_file)
  exchange_data_as_list = crypto_json_extract_obj.data_in_file_content
  for i, exchange in enumerate(exchange_data_as_list):
    print(str(i+1), ") ", exchange["name"]," (", exchange["id"], ") ", exchange["first_historical_data"])
  



def getTopExchangeNames(json_file, no):
  """This method returns a tuple with exchange names as a list and string
  
  Arguments:
  json_file : Path to the json file that contains exchange information
              retrived from coin market cap API
  no        : number of exchanges that user wants to see
  
  returns (exchange_names, exchange_names_one_string) tuple
  exchange_names            : A list containing exchange names
  exchange_names_one_string : Just adds all exchange names in the list 
                              mentioned above and comma between items
  """
  crypto_json_extract_obj = CryptoJsonExtract(json_file)
  exchange_data_as_list = crypto_json_extract_obj.data_in_file_content
  exchange_names = []
  for exchange in exchange_data_as_list[0:no]:
    exchange_names.append(exchange["name"])
  exchange_names_one_string = ",".join(exchange_names)
  return (exchange_names, exchange_names_one_string)




def getTopExchangeIds(json_file, no):
  """This method returns a tuple with exchange ids as a list and string
  
  Arguments:
  json_file : Path to the json file that contains exchange information
              retrived from coin market cap API
  no        : number of ids that user wants to see
  
  returns (exchange_ids, exchange_ids_one_string) tuple
  exchange_ids            : A list containing exchange ids
  exchange_ids_one_string : Just adds all exchange ids in the list 
                            mentioned above and comma between items
  """
  crypto_json_extract_obj = CryptoJsonExtract(json_file)
  exchange_data_as_list = crypto_json_extract_obj.data_in_file_content
  exchange_ids = []
  for exchange in exchange_data_as_list[0:no]:
    exchange_ids.append(str(exchange["id"]))
  exchange_ids_one_string = ",".join(exchange_ids)
  return (exchange_ids, exchange_ids_one_string)


def getExchangeInfo(json_file, exchange_id):
  """Returns a dict with all necessary information about an exchange
  
  information includes -
    - name
    - description
    - website
    - date_launched
    - spot_volume_usd
    - weekly_visits
    - maker_fee
    - taker_fee 
  """
  crypto_json_extract_obj = CryptoJsonExtract(json_file)
  exchange_data_as_list = crypto_json_extract_obj.data_in_file_content
  exchange_info_as_dict = {}
  exchange_info_as_dict["name"] = exchange_data_as_list[exchange_id]["name"]
  exchange_info_as_dict["description"] = exchange_data_as_list[exchange_id]["description"]
  exchange_info_as_dict["website"] = exchange_data_as_list[exchange_id]["urls"]["website"]
  exchange_info_as_dict["date_launched"] = exchange_data_as_list[exchange_id]["date_launched"]
  exchange_info_as_dict["spot_volume_usd"] = exchange_data_as_list[exchange_id]["spot_volume_usd"]
  exchange_info_as_dict["weekly_visits"] = exchange_data_as_list[exchange_id]["weekly_visits"]
  exchange_info_as_dict["maker_fee"] = exchange_data_as_list[exchange_id]["maker_fee"]
  exchange_info_as_dict["taker_fee"] = exchange_data_as_list[exchange_id]["taker_fee"]
  return exchange_info_as_dict




class CryptoJsonExtract():
  """ A simple class to contain extracted data from json file
  that stored information obtained from coin market cap API
  about exchanges
  """
  def __init__(self, input_json_file):
    self.input_json_file = input_json_file
    self.readInputFileAsJson()
    pass

  def readInputFileAsJson(self):
    with open(self.input_json_file, 'r') as f:
      file_content = f.read()
      self.file_content_as_dict = json.loads(file_content)
      self.data_in_file_content = self.file_content_as_dict["data"]
    return



def Main():
  #json_file = "v1.exchange.map.json"
  #showExchangeNames(json_file)
  #ex_names = getTopExchangeNames(json_file, 15)
  #print(ex_names)
  #ex_ids = getTopExchangeIds(json_file, 15)
  getExchangeInfo("v1.exchange.info.json", "102")
  #print(ex_ids)

if __name__ == "__main__":
  Main()