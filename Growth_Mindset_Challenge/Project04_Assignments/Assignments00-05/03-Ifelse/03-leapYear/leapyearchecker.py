def is_leap_year(year):
    """Check if a given year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    # user interface
    year = int(input("Enter a year: "))

    # Checking for a leap year
    if is_leap_year(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == "__main__":
    main()
