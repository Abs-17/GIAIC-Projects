
#''''''''''''''''''''''''''''''''' Password Generator with GUI '''''''''''''''''''''''''''

#Importing Libraries
import tkinter as tk
from tkinter import messagebox
import random
import string

def genpass():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_number = number_var.get()
    use_symbols = symbols_var.get()

    char = string.ascii_lowercase

    if use_uppercase:
        char += string.ascii_uppercase

    if use_number:
        char += string.digits

    if use_symbols:
        char += string.punctuation

    if len(char) == 0:
        messagebox.showerror("Error \n No character type selected for password generation")
        return
    
    passw = ''.join(random.choice(char)for _ in range(length))
    passw_entry.delete(0,tk.END)
    passw_entry.insert(0,passw)

#Creating the main window
root = tk.Tk()
root.title("Password Generator")

#Create the input fields and labels

length_label = tk.Label(root,text = "password length : ")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()


uppercase_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value = True)
symbols_var = tk.BooleanVar (value = True)


uppercase_check = tk.Checkbutton(root, text = "Include uppercase letters",variable= uppercase_var)
uppercase_check.pack()

number_check = tk.Checkbutton(root,text = "Include numbers" ,variable = number_var)
number_check.pack()

symbols_var = tk.Checkbutton(root,text = "Include symbols" , variable=symbols_var)
symbols_var.pack()



#create a button to generate the password

generate_button = tk.Button(root, text = "Generate Password" ,command = genpass)
generate_button.pack()


#create an entry field to display generated password

passw_entry = tk.Entry(root,width = 30)
passw_entry.pack()


#start GUI event loop
root.mainloop()



