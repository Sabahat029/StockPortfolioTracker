#Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "YOTU": 380,
    "INST": 450,
    "YAHO": 140,
    "FCBK": 270,
    "LKIN": 3900
}

# Get input from user
portfolio = {}

while True:
    stock = input("Enter stock symbol (YOTU, INST, YAHO, FCBK, LKIN): ").upper()
    if stock not in stock_prices:
        print("Invalid stock.Please Try again.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = quantity

    another = input("Do you want to add another stock? (yes/no): ").lower()
    if another != "yes":
        break

# Calculation for total investment
total_value = 0
print("\nYour Portfolio Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_value += investment
    print(f"{stock}: {quantity} shares x ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_value}")

# Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write("portfolio Summary:\n")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock}: {quantity} shares x ${price} = ${investment}\n")
    file.write(f"\nYour Total Investment Value is: ${total_value}")

    print("\nPortfolio summary saved to 'portfolio_summary.txt'")
