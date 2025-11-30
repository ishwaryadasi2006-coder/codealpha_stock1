# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 310
}

# Dictionary to store user portfolio
portfolio = {}

# Take user input
print("Enter your stock portfolio. Type 'done' when finished.\n")
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print(f"Stock '{stock}' not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            raise ValueError
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid positive integer for quantity.")

# Calculate total investment
total_investment = 0
print("\nYour Stock Portfolio:")
print("-----------------------")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print("-----------------------")
print(f"Total Investment Value: ${total_investment}")

# Optional: Save to file
save = input("\nWould you like to save the result to a file? (yes/no): ").lower()
if save in ['yes', 'y']:
    filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
    try:
        with open(filename, "w") as file:
            file.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                file.write(f"{stock},{qty},{price},{value}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}")
        print(f"Portfolio saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving file: {e}")
