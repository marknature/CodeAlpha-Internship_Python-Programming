def calculate_portfolio_value():
    """
    Calculates the total investment value of a stock portfolio based on user input and hardcoded stock prices.
    """

    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 2500,
        "AMZN": 150
    }

    portfolio = {}

    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").upper()
        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Invalid stock name. Please choose from: ", list(stock_prices.keys()))
            continue

        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for quantity.")

        portfolio[stock_name] = quantity

    total_value = 0
    print("\nPortfolio:")
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        print(f"{stock}: {quantity} x ${price} = ${value}")
        total_value += value

    print(f"\nTotal Portfolio Value: ${total_value}")

    # Optional: Save to file
    save_to_file = input("Save portfolio value to file? (y/n): ").lower()
    if save_to_file == 'y':
        filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
        try:
            with open(filename, 'w') as f:
                f.write("Stock,Quantity,Price,Value\n")
                for stock, quantity in portfolio.items():
                    price = stock_prices[stock]
                    value = price * quantity
                    f.write(f"{stock},{quantity},{price},{value}\n")
                f.write(f"Total:,${total_value}\n")
            print(f"Portfolio value saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

