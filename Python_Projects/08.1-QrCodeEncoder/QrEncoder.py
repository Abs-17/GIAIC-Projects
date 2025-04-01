#Libraries
import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image


def generate_qr_code(data):
    """Genereating a QR code from a given data and displaying it"""
    #Creating a QR code instance
    try:
        qr = qrcode.QRCode(
        #Controls the size of the QR Code
        version = 1,
        #Error Correction Level
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        #Size of pixels in each box
        box_size= 10,
        #Thickness of the border of the image 
        border=5
        )
        #Add data to the QR Code
        qr.add_data(data)
        qr.make(fit=True)

        #Creating an image from the QR code instance
        qr_image = qr.make_image(fil_color='black',second_color ='white')

        file_path = "qrcode.png"
        qr_image.save(file_path)

        #Loading the image to show in Tkinter
        image_tk = ImageTk.PhotoImage(Image.open(file_path))
        qr_code_label.config(image=image_tk)
        #keepig a reference to avoid garbage collection
        qr_code_label.image=image_tk 

        #pop up message box
        messagebox.showinfo("Success !", "QR CODE generated and saved as 'qrcode.png'.")
    except Exception as e:
        messagebox.showinfo("Error !", f"An error occured {e}:")

def upon_generate():
    """Handling the Generate button click event"""
    data = entry.get()
    if(data):
        generate_qr_code(data)
    else:
        messagebox.showwarning("Input error", "Re-enter data to generate QR CODE")

# Creating the main Window
root = tk.Tk()
root.title("QR CODE GENERATOR")
root.geometry("400x500")

#Creating an entry field for user input
entry_label = tk.Label(root,text ="Enter URL or text: ")
entry_label.pack(pady=10)

entry = tk.Entry(root,width= 50)
entry.pack(pady=10)

# Create a generate button
generate_button = tk.Button(root, text="Generate QR Code", command=upon_generate)
generate_button.pack(pady=10)

# Label to display the QR code
qr_code_label = tk.Label(root)
qr_code_label.pack(pady=20)

# Run the application
root.mainloop()


        
   

    
    
