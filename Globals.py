#!/usr/bin/env python3
db_transaction_path   = "./transaction_sheet.csv"
db_transaction_header = "transaction_type,bought coin symbol,bought coin amount," + \
                        "bought coin unit price,sold coin symbol,sold coin amount," + \
                        "sold coin unit price,total spending in fiat"

db_balances_path        = "./balance_sheets.csv"
db_balances_path_header = "symbol, total amount holding, average per unit price, "+ \
                          "fiat spending(based on average data), past profit"
