from array import array
from datetime import datetime

class Config:
  def __init__(self, args: array):
    if len(args) != 4:
      raise Exception("Invalid number of commands. Needing: file name, begin date, end date, dca amount.")

    self.doc_name: str = args[0]
    self.begin: datetime = datetime.strptime(args[1], '%Y-%m-%d')
    self.end: datetime = datetime.strptime(args[2], '%Y-%m-%d')
    self.dca_amount: float = float(args[3])
    self.total_bought: float = 0

  def date_witin_range(self, date: str) -> bool:
    date = datetime.strptime(date, '%Y-%m-%d')
    return self.begin <= date <= self.end