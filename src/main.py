import sys
from config import Config
from commands import print_all_coins, begin_analysing_csv, print_output

def main():
  args = sys.argv
  if args[1] == 'list':
    print_all_coins()
  elif args[1] == 'dca':
    config = Config(args[2:])
    begin_analysing_csv(config)
    print_output(config)
  else:
    print("unknown command")

if __name__ == '__main__':
  main()
