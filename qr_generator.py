import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Testing example:
# myQR = qrcode.make("https://www.youtube.com/watch?v=PyDn2gU9DJo")
# myQR.save("myQR.png")

my_QR = input("Enter the text to encode in QR code: ")
myQR = qrcode.make(my_QR)
myQR.save("myQR.png")

# decoded_objects = decode(Image.open("myQR.png"))
# print(decoded_objects[0].data.decode("ascii"))
