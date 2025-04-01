def divide_numbers():
    """Prompts the user for two integers and calculates division result and remainder."""
    try:
        # user interface
        num1 = int(input("\033[1;3;4mPlease enter an integer to be divided:\033[0m "))  
        num2 = int(input("\033[1;3;4mPlease enter an integer to divide by:\033[0m "))  

        # Preventing division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return  

        # quotient and remainder
        quotient = num1 // num2
        remainder = num1 % num2

        #  results
        print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

    except ValueError:
        print("Invalid input! Please enter valid integers.")


divide_numbers()
