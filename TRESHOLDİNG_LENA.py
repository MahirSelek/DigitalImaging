from PIL import Image
#open image file
im_name="LENA.jpg"
img=Image.open(im_name)
img = img.convert("L")

#new size
w = img.size[0]
h = img.size[1]

 
pixel = img.load()

#create binary lena-tresholding

binary="binary_lena.jpg"
for i in range (w):
    for j in range(h):
        if pixel[i,j]>90 and pixel[i,j]<170:
            pixel[i,j]=255
        else:
                pixel[i,j]=0
img.save(binary)
img.show()
