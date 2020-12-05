from PIL import Image


#open lena image file

img_name="CAT.jpg"
img=Image.open(img_name)
img=img.convert("L")

#size of image

w=img.size[0]
h=img.size[1]
pixel = img.load()
#create negative lena

negative="negative_cat.jpg"
img=Image.open(img_name)
img=img.convert("L")
pixels=img.load()
negative_img=Image.new(img.mode ,img.size,color=0)
for i in range(w):
    for j in range(h):
        pixels[i,j]=255-pixels[i,j]
        negative_img.putpixel((i,j),pixels[i,j])
negative_img.save(negative)
negative_img.show()

