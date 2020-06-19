import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

min_size = 50
max_size = 80
min_x_y = 0
max_x_y = 120
min_x_tri = 50
max_x_tri = 150
min_y_tri = 0
max_y_tri = 150

drive_path = '<path to dir>'

squ_dest = drive_path+'squares/'
cir_dest = drive_path+'circles/'
tri_dest = drive_path+'triangles/'

for i in range(4096):
    if i%300 == 0:
        print(i)
    x = np.random.randint(min_x_y, max_x_y)
    y = np.random.randint(min_x_y, max_x_y)
    r = np.random.randint(min_size, max_size)
    x_tri_1 = np.random.randint(min_x_tri, max_x_tri)
    y_tri_1 = np.random.randint(min_y_tri, max_y_tri)
    x_tri_2 = x_tri_1 + int(r/1.5)
    y_tri_2 = y_tri_1 + r
    x_tri_3 = x_tri_1 - int(r/1.5)

    img1 = Image.new('L', (200,200), (0))
    ImageDraw.Draw(img1).rectangle((x, y, x+r, y+r), fill=255)
    img1 = img1.filter(ImageFilter.GaussianBlur(radius = 3))
    
    img2 = Image.new('L', (200,200), (0))
    ImageDraw.Draw(img2).ellipse((x, y, x+r, y+r), fill=255)
    img2 = img2.filter(ImageFilter.GaussianBlur(radius = 3)) 
    
    img3 = Image.new('L', (200,200), (0))
    ImageDraw.Draw(img3).polygon([(x_tri_1,y_tri_1), (x_tri_2, y_tri_2), (x_tri_3, y_tri_2)], fill = 255)
    img3 = img3.filter(ImageFilter.GaussianBlur(radius = 3)) 

    img1.save(squ_dest+str(i)+".png", "PNG")
    img2.save(cir_dest+str(i)+".png", "PNG")
    img3.save(tri_dest+str(i)+".png", "PNG")
