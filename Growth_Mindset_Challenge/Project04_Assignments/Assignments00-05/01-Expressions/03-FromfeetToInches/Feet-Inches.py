def feet_to_inches():
    print("The feet to Inches Convertor")

    #user interface
    feet = float(input("Enter feet for conversion: "))
    
    #conversion
    inches = feet * 12

    print(f'Converting.......\nYour given Feet is {feet} and after converting to Inches = {inches}')

if __name__=='__main__':
    feet_to_inches()

