# CodeAlpha Task 2 - Stock Portfolio Tracker

portfolio = []

while True:
    print("\n===== STOCK PORTFOLIO TRACKER =====")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Calculate Total Investment")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter stock name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter buy price: "))

        stock = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

        portfolio.append(stock)
        print("Stock added successfully!")

    elif choice == "2":
        if len(portfolio) == 0:
            print("Portfolio is empty.")
        else:
            print("\n----- YOUR PORTFOLIO -----")

            for stock in portfolio:
                value = stock["quantity"] * stock["price"]

                print("Stock:", stock["name"])
                print("Quantity:", stock["quantity"])
                print("Buy Price:", stock["price"])
                print("Investment:", value)
                print("----------------------")

    elif choice == "3":
        total = 0

        for stock in portfolio:
            total += stock["quantity"] * stock["price"]

        print("Total Investment:", total)

    elif choice == "4":
        print("Thank you for using Stock Portfolio Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
