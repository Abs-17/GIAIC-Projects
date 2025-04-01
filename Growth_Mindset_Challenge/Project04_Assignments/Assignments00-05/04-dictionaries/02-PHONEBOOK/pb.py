def read_phonebook():
    """
    Collect names and numbers from the user and store them in a dictionary.
    Returns the populated phonebook.
    """
    phonebook = {}

    while True:
        name = input("Enter contact name (or press Enter to stop): ").strip()
        if not name:
            break
        if name in phonebook:
            print(f"{name} already exists. Updating the number.")
        number = input(f"Enter {name}'s phone number: ").strip()
        phonebook[name] = number

    return phonebook


def display_phonebook(phonebook):
    """
    Displays all contacts in the phonebook in a sorted manner.
    """
    if not phonebook:
        print("Phonebook is empty.")
        return

    print("\nPhonebook:")
    for name in sorted(phonebook.keys()):
        print(f"{name} -> {phonebook[name]}")


def find_number(phonebook):
    """
    Allows the user to look up a contact’s phone number.
    """
    while True:
        name = input("\nEnter name to look up (or press Enter to exit): ").strip()
        if not name:
            break
        print(phonebook.get(name, f"{name} is not in the phonebook."))


def main():
    print("Welcome to the Phonebook App!")
    phonebook = read_phonebook()
    display_phonebook(phonebook)
    find_number(phonebook)
    print("\nThank you for using the Phonebook App!")


# Run the program
if __name__ == "__main__":
    main()

