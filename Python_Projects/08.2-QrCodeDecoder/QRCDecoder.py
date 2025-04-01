#Libraries
import tkinter as tk
from tkinter import filedialog, messagebox
from pyzbar.pyzbar import decode
from PIL import Image

def decoding_qr_code(img_path):
    """Decoding the QR Code from the provided image and retrieving the data from it..."""
    try:
        img = Image.open(img_path)
        decode_objects = decode(img)
        if decode_objects:
            message = [obj.data.decode('utf-8') for obj in decode_objects]
            return'\n'.join(message)
        else:
            return'No QR Code found.'
    except Exception as e:
        return f"An error has occurred {e}"

def upon_upload():
    """Handling the upload button click event"""
    File_path = filedialog.askopenfilename(title="Select a QR Code Image",filetypes = [("Image files","*.png;*.jpg;*.jpeg;*.bmp")])

    if File_path:
        result = decoding_qr_code(File_path)
        result_label.config(text=result)

#Creating the main window
root = tk.Tk()
root.title("The QR Code Decoder")
root.geometry("400x300")

#Creating a label to inform the user
info_label = tk.Label(root, text ="Upload a QR Image to decode it :")
info_label.pack(pady = 10)

#Create an upload button
upload_button = tk.Button(root, text="Upload QR Code Image", command=upon_upload)
upload_button.pack(pady=10)

#Label to display the decoded message
result_label = tk.Label(root, text=" ",wraplength=300)
result_label.pack(pady=20)

#Run the application
root.mainloop()

