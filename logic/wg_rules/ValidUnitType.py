
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  if self.unit_type not in ['unit', 'kg', 'liter', 'meter']:
      raise ValueError('Invalid unit type.')
