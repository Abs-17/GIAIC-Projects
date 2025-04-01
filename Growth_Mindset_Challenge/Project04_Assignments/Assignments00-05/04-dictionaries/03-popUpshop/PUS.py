def calculate_fruit_cost():
    """
    Asks the user for the quantity of each fruit they want to buy
    and calculates the total cost.
    """
    fruit_prices = {
        "apple": 5.0,
        "durian": 15.0,
        "jackfruit": 12.5,
        "kiwi": 8.0,
        "rambutan": 6.5,
        "mango": 10.0
    }

    total_cost = 0

    print("Welcome to the Fruit Shop Calculator!\n")

    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: ").strip())
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                total_cost += quantity * price
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    print(f"\nYour total is ${total_cost:.2f}")



if __name__ == "__main__":
    calculate_fruit_cost()
