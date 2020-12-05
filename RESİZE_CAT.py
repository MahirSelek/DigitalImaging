import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

#resized image

img1=cv2.imread("CAT.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("CAT",img1)
height=len(img1)
width=len(img1[0])
factor=4

nwidth=width//factor
nheight=height//factor

img2=np.zeros((nheight,nwidth,1))
print(nheight ,nwidth)
for i in range (nheight):
    for j in range (nwidth):
        img2[i,j]=img2[(i//factor),(j//factor)]
    print(j,i)

