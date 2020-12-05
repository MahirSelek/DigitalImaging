from PIL import Image


#open lena image file

img_name="CAT.jpg"
img=Image.open(img_name)
img=img.convert("L")

#size of image

w=img.size[0]
h=img.size[1]

#flip image
pixel = img.load()
flip="flipped_cat.jpg"
flipped_img=Image.new(img.mode ,img.size,color=0)
for i in range(w):
    for j in range(h):
        flipped_img.putpixel((i,j),pixel[i,w-1-j])
flipped_img.save(flip)
flipped_img.show()

