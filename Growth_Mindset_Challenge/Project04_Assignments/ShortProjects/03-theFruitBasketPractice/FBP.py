def main():
    # A list called fruit_list that contains the specified fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    print("Fruit list:", fruit_list)
    
    # Adding 'mango' to the list
    fruit_list.append('mango')
    print("After adding mango:", fruit_list)
    
    # Removing 'banana' from the list
    fruit_list.remove('banana')
    print("After removing banana:", fruit_list)
    
    # Printing the first and last fruit in the list
    print("First fruit:", fruit_list[0])
    print("Last fruit:", fruit_list[-1])
    
    # Print in alphabetical order (without modifying the original list)
    print("Alphabetically sorted:", sorted(fruit_list))
    
    # Print in reverse order (modifying the original list)
    fruit_list.reverse()
    print("Reversed list:", fruit_list)


main()
