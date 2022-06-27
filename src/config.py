from array import array
from datetime import datetime

class Config:
  def __init__(self, args: array):
    if len(args) != 5:
      raise Exception("Invalid number of commands. Needing: file name, begin date, end date, dca amount, sell at price.")

    self.doc_name: str = args[0]
    self.begin: datetime = datetime.strptime(args[1], '%Y-%m-%d')
    self.end: datetime = datetime.strptime(args[2], '%Y-%m-%d')
    self.dca_amount: float = float(args[3])
    self.sell_at_price: float = float(args[4])

    self.total_bought: float = 0
    self.spent_for_period: float = 0
    self.total_value_at_price: float = 0

  def date_witin_range(self, date: str) -> bool:
    date = datetime.strptime(date, '%Y-%m-%d')
    return self.begin <= date <= self.end