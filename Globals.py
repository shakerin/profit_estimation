#!/usr/bin/env python3
db_transaction_path   = "./transaction_sheet.csv"
db_transaction_header = "transaction_type,bought coin symbol,bought coin amount," + \
                        "bought coin unit price,sold coin symbol,sold coin amount," + \
                        "sold coin unit price,total spending in fiat"

db_balances_path        = "./balance_sheets.csv"
db_balances_path_header = "symbol, total amount holding, average per unit price, "+ \
                          "fiat spending(based on average data), past profit"


# colors for terminal
RED   = "\033[0;31;49m"
GREEN = "\033[0;32;49m"
BLUE  = "\033[0;34;49m"
WHITE = "\033[0;37;49m"
BLACK = "\033[0;30;49m"

RED_BOLD   = "\033[1;31;49m"
GREEN_BOLD = "\033[1;32;49m"
BLUE_BOLD  = "\033[1;34;49m"
WHITE_BOLD = "\033[1;37;40m"
BLACK_BOLD = "\033[1;30;49m"
