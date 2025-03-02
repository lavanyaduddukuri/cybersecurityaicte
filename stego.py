import cv2
import os
import string

img = cv2.imread("image.jpg")
height, width, _ = img.shape
img_size = height * width * 3

msg = input("Enter secret message:")
password = input("Enter a passcode:")

if len(msg) * 8 > img_size:
    print("Error: The image is too small to hold the message.")
    exit()

d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

n = 0
m = 0
z = 0
for i in range(len(msg)):
    char_val = d[msg[i]]
    img[n, m, z] = (img[n, m, z] & 0xFE) | (char_val >> (i % 8) & 1)
    m += 1
    if m >= width:
        m = 0
        n += 1
    if n >= height:
        break
    z = (z + 1) % 3

cv2.imwrite("encryptedimage.jpg", img)
os.system("start encryptedimage.jpg")

message = ""
pas = input("Enter passcode for Decryption: ")
if password == pas:
    n = 0
    m = 0
    z = 0
    for i in range(len(msg)):
        char_val = (img[n, m, z] & 1) << (i % 8)
        message += c[char_val]
        m += 1
        if m >= width:
            m = 0
            n += 1
        if n >= height:
            break
        z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
