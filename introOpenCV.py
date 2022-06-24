# Reading an image
import cv2

image_path='./input_image/road.jpg'
image=cv2.imread(image_path)
h,w=image.shape[:2]#give first=height,second=width
print(image)
print("\nImage width={} and height={}".format(w,h))
cv2.namedWindow("image_window",cv2.WINDOW_NORMAL)
cv2.resizeWindow("image_window",500,500)
cv2.imshow('image_window',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
window_name='image_window'
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()# closing all open windows
'''

#Extracting the RGB values of a pixel
(B,G,R)=image[200,150]
print("R = {},G = {},B = {}".format(R,G,B))
print("Green Channel = {}".format(G))
print("Red = {}".format(image[200,150,2]))
B = image[100, 100, 0]
print("Blue channel={}".format(B))


#Extracting the region of Interest(ROI)
roi=image[100 : 500, 200 : 700] #slicing the pixel of the image
window_name = 'image_roi'
cv2.namedWindow("roi_window",cv2.WINDOW_NORMAL)
cv2.resizeWindow("roi_window",500,500)
cv2.imshow('roi_window', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Resizing the Image
resize_image=cv2.resize(image,(1500,1500))# cv2.resize(image,(w,h))
hr,wr=resize_image.shape[:2]
print("Resize_image_Width={}, Resize_image_height={}".format(wr,hr))
cv2.namedWindow('resize_image_window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('resize_image_window',500,500)
cv2.imshow('resize_image_window',resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()# closing all open windows


#same image aspect ratio
ratio=800/w
dim=(800,int(h * ratio))
new_ratio_image=cv2.resize(image,dim)
nh,nw=new_ratio_image.shape[:2]
print("new_raito_image_Width={} and new_ratio_image_Height={}".format(nw,nh))
cv2.namedWindow('new_ratio_image_window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('new_ratio_image_window',500,500)
cv2.imshow('new_ratio_image_window', new_ratio_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Rotating the Image
center=(w//2,h//2)#calculating the center of image
matrix=cv2.getRotationMatrix2D(center,-45,1) #generating a rotation matrix
rotated_image=cv2.warpAffine(image,matrix,(w,h))# wrap image with rotation matrix
cv2.namedWindow("rotated_image_window",cv2.WINDOW_NORMAL)
cv2.resizeWindow("rotated_image_window",500,500)
cv2.imshow("rotated_image_window", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()# closing all open windows


# drawing a Rectangle
rectangle=image.copy()
rectangle=cv2.rectangle(rectangle,(800,750),(1500,1200),(0,0,255),5)
cv2.namedWindow("drawing_rectangle_window",cv2.WINDOW_NORMAL)
cv2.resizeWindow("drawing_rectangle_window",500,500)
cv2.imshow("drawing_rectangle_window",rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

# displaying text
text=image.copy()
cv2.namedWindow("displaying_text_window",cv2.WINDOW_NORMAL)
cv2.resizeWindow("displaying_text_window", 500,500)
text=cv2.putText(text,'Intro OpenCV',(400,750),cv2.FONT_HERSHEY_SIMPLEX,5,(255,0,0),10)
cv2.imshow("displaying_text_window",text)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("END")
