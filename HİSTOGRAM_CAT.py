from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

img_name="CAT.jpg"
img=cv2.imread(img_name)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
size_y=img.shape[0]
size_x=img.shape[1]
flattened=img.reshape([size_x*size_y])
rhist,_,_=plt.hist(flattened,bins=128)
plt.show()

