def add_three_copies(lst, data):
    """Adds three copies of data to list without returning anything"""
    lst.append(data)
    lst.append(data)
    lst.append(data)

# Example usage
messages = []
user_input = input("Enter a message to copy: ")

print("\nList before:", messages)
add_three_copies(messages, user_input)
print("List after:", messages)
