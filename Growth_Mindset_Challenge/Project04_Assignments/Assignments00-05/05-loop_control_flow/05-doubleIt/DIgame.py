def double_number():
    """Asks the user for a number and doubles it until it reaches 100 or more"""
    try:
        curr_value = int(input("Enter a number to start doubling: "))
        
        if curr_value <= 0:
            print("⚠️ Please enter a positive number!")
            return
        
        print("\nDoubling sequence:")
        while curr_value < 100:
            curr_value *= 2
            print(curr_value, end=" ")

        print("\n🎯 Stopped! The number reached or exceeded 100.\n")

    except ValueError:
        print("⚠️ Invalid input! Please enter a valid integer.")

def main():
    """ function to control program execution"""
    print("\n🔢 Welcome to the Number Doubling Game! 🎲\n")

    while True:
        double_number()
        again = input("Do you want to try again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n👋 Thanks for playing! See you next time. 😊")
            break

if __name__ == "__main__":
    main()
