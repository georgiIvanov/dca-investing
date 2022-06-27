import sys
from config import Config
from commands import print_all_coins, begin_analysing_csv


if __name__ == '__main__':
  args = sys.argv
  if args[1] == 'list':
    print_all_coins()
  elif args[1] == 'dca':
    begin_analysing_csv(Config(args[2:]))
  else:
    print("unknown command")
