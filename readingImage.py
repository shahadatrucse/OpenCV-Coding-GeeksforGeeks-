import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt


# read image using cv2 and show using cv2
image_path='./tomato.png'
image=cv2.imread(image_path,1)
'''
window_name="reading_image_window"
cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name,500,500)
cv2.imshow(window_name,image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
cv2.imshow("image_window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# read image using cv2 and show using plt
plt.figure(figsize=(50,50))
plt.subplot(2,2,1)
plt.title("read cv2 & show plt",fontsize=50)
plt.imshow(image)


# cv2--BGR to RGB
rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.subplot(2,2,2)
plt.title("BGR to RGB",fontsize=50)
plt.imshow(rgb_image)


# read in grayscale mode
new_image=cv2.imread(image_path,0)#parametar 0 use for taking image grayscale mode 
plt.subplot(2,2,3)
plt.title("read in grayscale mode",fontsize=50)
plt.imshow(new_image,cmap='gray')

# grayscale image show using cv2
cv2.imshow("Grayscale_window",new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


plt.savefig("reading_image_usingCV2.jpg")