from stegano import lsb
from PIL import Image
import os
image_file = input("Enter image file name: ")
while not os.path.isfile(image_file):
    print("File not found. Please try again.")
    image_file = input("Enter image file name: ")

secret_message = input("Enter secret message: ")

image = Image.open(image_file)

steg_image = lsb.hide(image, secret_message)

extracted_message = lsb.reveal(steg_image)

if extracted_message == secret_message:
    print("Message successfully embedded in image.")
else:
    print("Error: Failed to embed message in image.")

steg_image.save('steg_image.png')
