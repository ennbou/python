import sys
from PIL import Image

imagePath = "file1.png"

img = Image.open("C:\\Users\\DJK\\Documents\\Python\\img\\file1.png")
img.show()

colonne,ligne = img.size()

for i in range(ligne):
    for j in range(colonne):
        pixel = img.getpixel((j, i))  # récupération du pixel
        p = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
        img.putpixel((j, i), p)


'''
7 question de coures

'''

