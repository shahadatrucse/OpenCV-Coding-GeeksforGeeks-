import cv2
import os

source='./input_image/road.jpg'
destination='/home/shahadat/Desktop/DIP'
image=cv2.imread(source)

os.chdir(destination)#change directory for destination
print("Before wirte image in destination")
print(os.listdir(destination))#show all file of destination folder

filename = 'writeImage.jpg'#image filename which name use for save image in destination
cv2.imwrite(filename, image)# image write in destination

print("After wirte image in destination")
print(os.listdir(destination))
print("Write image in destination successfully")
