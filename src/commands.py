import csv
import os
from typing import Iterator
from config import Config

def coins_path(coin: str):
  current = os.getcwd()
  coins_path = os.path.join(current, 'top_coins_price_feed')

  if coin is not None and coin != "":
    return os.path.join(coins_path, coin)
  else:
    return coins_path


def print_all_coins():
  all_coins = coins_path(None)

  for f in os.listdir(all_coins):
    if os.path.isfile(os.path.join(all_coins, f)) & f.endswith('.csv'):
      print(f)

def begin_analysing_csv(config: Config):
  doc_path = coins_path(config.doc_name)
  if os.path.exists(doc_path) == False: 
    print('File does not exist: {0}', doc_path)
    return -1

  with open(doc_path, 'r') as file:
    csvreader = csv.reader(file)  
    _ = next(csvreader)
    iterate_data(csvreader, config)

def iterate_data(iter: Iterator, config: Config):
  rows_in_range = []
  total_bought = 0
  for row in iter:
    date = row[0]
    if config.date_witin_range(date):
      rows_in_range.append(row)
      # Right now the Open price is used
      # but you can use any other by changing the index
      # or you can calculate an average
      bought_that_day = (1 / float(row[1])) * config.dca_amount
      total_bought += bought_that_day
  
  config.total_bought = total_bought
  print('Total bought for period ', total_bought)
  