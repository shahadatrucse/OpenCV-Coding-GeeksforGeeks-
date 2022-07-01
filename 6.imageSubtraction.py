import cv2

def main():
    image_path1='./input_image/sub.jpg'
    image_path2='./input_image/sub1.jpg'
    
    image1=cv2.imread(image_path1)
    image2=cv2.imread(image_path2)
    
    subImage=cv2.subtract(image1,image2)
    
    cv2.imshow("Image Subtraction",subImage)
    cv2.imwrite("./output_image/6.imageSubtraction.jpg",subImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
if __name__=='__main__':
    main()