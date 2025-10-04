def stock_portfolio():
    # Hardcoded stock prices (dictionary)
    stock_prices = {
        "apple": 180,
        "google": 2700,
        "microsoft": 300,
        "tesla": 750,
        "amazon": 3300
    }

    portfolio = {}  # To store user's stocks
    print("\n📈 Welcome to Stock Portfolio Tracker!\n")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"- {stock.capitalize()}: ${price}")

    print("\nEnter your stocks (type 'done' to finish):")

    while True:
        stock = input("\nEnter stock name: ").lower().strip()

        if stock == "done":
            break

        if stock not in stock_prices:
            print("⚠️ Stock not available. Please choose from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock.capitalize()}: "))
            if quantity <= 0:
                print("⚠️ Quantity must be greater than 0.")
                continue
        except ValueError:
            print("⚠️ Invalid input! Please enter a number for quantity.")
            continue

        # Add to portfolio
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"✅ Added {quantity} shares of {stock.capitalize()}.")

    # Calculate portfolio value
    if not portfolio:
        print("\n📂 Your portfolio is empty.")
        return

    print("\n📊 Your Portfolio Summary:")
    total_value = 0
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        total_value += value
        print(f"- {stock.capitalize()} ({qty} shares) = ${value}")

    print(f"\n💰 Total Portfolio Value: ${total_value}")

    # Save to file
    save = input("\nDo you want to save the result to a file? (y/n): ").lower()
    if save == "y":
        with open("portfolio_summary.txt", "w") as file:
            file.write("📊 Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = qty * price
                file.write(f"{stock.capitalize()} ({qty} shares) = ${value}\n")
            file.write(f"\n💰 Total Portfolio Value: ${total_value}\n")
        print("✅ Portfolio saved to portfolio_summary.txt")


# Run program
if __name__ == "__main__":
    stock_portfolio()
