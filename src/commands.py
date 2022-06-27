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
      
      # also called typical price = (H+L+C)/3
      typical_price_average = (float(row[2]) + float(row[3]) + float(row[4])) / 3
      bought_that_day = (1 / typical_price_average) * config.dca_amount
      total_bought += bought_that_day
  
  config.spent_for_period = len(rows_in_range) * config.dca_amount
  config.total_bought = total_bought
  config.total_value_at_price = config.sell_at_price * total_bought

def print_output(config: Config):
  print('You would have spent', config.spent_for_period, '$')
  print('Total coin bought for period', config.total_bought)
  print('If you sold at', config.sell_at_price, 'you would have made', config.total_value_at_price)

  percentage = config.total_value_at_price / config.spent_for_period

  if percentage > 1:
    print('This would make a', percentage, 'times the return')
  else:
    print('Oh oooh, not a good deal. You would get', percentage, 'times the return')