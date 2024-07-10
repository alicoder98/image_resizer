import cv2
import os
import glob
import matplotlib.pyplot as plt
path1 = "img640/"
path2="img3200/"
if not os.path.isdir(path1):
    os.makedirs(path1)
if not os.path.isdir(path2):
    os.makedirs(path2)
for img in glob.glob("image/*.jpg"):
    image= cv2.imread(img,1)
    cv2.waitKey(0)
    strname=str(os.path.basename(img))
    
    newimg640=cv2.resize(image, (640, 640))
    newimg3200=cv2.resize(image, (3200, 3200))
    #imgplot = plt.imshow(newimg)
    #plt.show()
    cv2.imwrite(path1+strname,newimg640)
    cv2.imwrite(path2+strname,newimg3200)



