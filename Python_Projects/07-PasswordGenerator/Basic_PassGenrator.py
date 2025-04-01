
#''''''''''''''''''''' Password Generator '''''''''''''''''''''''''''''

#importing libraries
import random
import string

def genpass(length,use_uppercase = True, use_numbers = True, use_symbols = True):
    char = string.ascii_lowercase  #to start with lowercase leters

    if use_uppercase:
        char += string.ascii_uppercase  #to add uppercase
    if use_numbers:
        char += string.digits      #to add numbers
    if use_symbols:
        char += string.punctuation   # to add symbols

    if len(char) == 0:
        raise ValueError("No character type selected for password generation")
    
    #generate password
    passw = ''.join(random.choice(char) for _ in range (length))

    return passw

#Inputation from the user

length = int(input("Enter the length of your password: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

#Generate and print password

passw = genpass(length,use_uppercase,use_numbers,use_symbols)
print('generated password :', passw)