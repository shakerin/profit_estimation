from Globals import *

def setupEnv():
  with open(db_transaction_path, 'w') as f:
    f.write(db_transaction_header)
  with open(db_balances_path, 'w') as f:
    f.write(db_balances_path_header)