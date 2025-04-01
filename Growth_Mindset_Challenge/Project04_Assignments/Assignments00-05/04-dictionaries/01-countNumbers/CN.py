#Library
from collections import defaultdict

def count_numbers():
    '''Count occurrences of user-entered numbers until an empty input is given.'''
    number_count = defaultdict(int)
    while True:
        num = input("Enter a number: ").strip()
        if not num:  # Stop when user enters nothing
            break
        if num.isdigit():  # Ensure valid numeric input
            number_count[int(num)] += 1
        else:
            print("Invalid input. Please enter a valid number.")

    print("\nNumber occurrences:")
    for number, count in sorted(number_count.items()):
        print(f"{number} appears {count} times.")

count_numbers()