from email.mime import image
import numpy as np
import cv2

def main():
    image_path1='./input_image/add1.jpg'
    image_path2='./input_image/add2.jpg'
    
    image1=cv2.imread(image_path1)
    image2=cv2.imread(image_path2)
    
    sumweighted=cv2.addWeighted(image1,0.5,image2,0.4,0)
    cv2.imshow("sumWeighted Image",sumweighted)
    cv2.imwrite("./output_image/5.imageAdd_Sub.jpg",sumweighted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
    




if __name__=='__main__':
    main()