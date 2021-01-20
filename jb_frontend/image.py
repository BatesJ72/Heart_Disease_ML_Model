import math 
from PIL import Image, ImageDraw

# Add Shape
w, h = 220, 190
shape = [(40, 40), (w - 10, h - 10)] 

# creating new Image object 
img = Image.new("RGB", (w, h)) 

def shape(data):
    if data[0] > 50:
        img1 = ImageDraw.Draw(img)   
        img1.rectangle(shape, fill ="red") 
        img.show() 
    else: 
        img1 = ImageDraw.Draw(img)   
        img1.rectangle(shape, fill ="green") 
        img.show() 