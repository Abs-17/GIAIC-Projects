def main():
    # Ask the user for their age
    age = int(input("How old are you? "))

    # Voting ages in different countries
    voting_ages = {
        "Peturksbouipo": 16,
        "Stanlau": 25,
        "Mayengua": 48
    }

    # Check voting eligibility for each country
    for country, required_age in voting_ages.items():
        if age >= required_age:
            print(f"You can vote in {country} where the voting age is {required_age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {required_age}.")

if __name__ == "__main__":
    main()
