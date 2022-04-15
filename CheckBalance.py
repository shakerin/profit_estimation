from ReadStoredBalances import readStoredBalances

def checkBalance(symbol):
  coin_info = readStoredBalances()
  symbols, total_amounts, prices, fiat_spendings, past_profits = coin_info
  if symbol in symbols:
    index = symbols.index(symbol)
    total_amount_stored = str(total_amounts[index])
    price_stored = str(prices[index])
    fiat_spending_stored = str(fiat_spendings[index])
    past_profit = str(past_profits[index]).strip()
    if past_profit == "":
        past_profit = "0"
    print("Current balance of        "+symbol+" = "+total_amount_stored)
    print("Current price per unit of "+symbol+" = "+price_stored)
    print("Current fiat value of     "+symbol+" = "+fiat_spending_stored)
    print("Past profit from trading  "+symbol+" = "+past_profit)
  else:
    print("No existing balance available for " + symbol)