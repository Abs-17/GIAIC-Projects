#importing qrcode package from library to make a qrcode
import qrcode


#Making a function to generate a qrcode within the specified elements
def gen_Qr(data,fileName):
    qr = qrcode.QRCode(
        #for controlling the size of the box
        version = 1,            
        #For Correcting any inmaking error
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        #for controlling the size of each pixel
        box_size = 10,
        #Border size
        border = 4,
    )

    #Adding data to the Qr Code
    qr.add_data(data)
    qr.make(fit = True)

    # For Generating a pixelated image for the code
    image = qr.make_image(fill = "black", bg_color = "white")

    #saving image to file
    image.save(fileName)
    print(f'QR Code saved as {fileName}')

# Testing

# Provide data to encode
data = "https://www.instagram.com/data_dabbler_basit/"
fileName = "my profile.png"
gen_Qr(data,fileName)
