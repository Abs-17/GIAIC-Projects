def get_first_element(lst):
    """Prints the first element of the list"""
    print("The first element is:", lst[0])

# user interface 
user_list = []
num_elements = int(input("Enter the number of elements in the list: "))

for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)


get_first_element(user_list)
