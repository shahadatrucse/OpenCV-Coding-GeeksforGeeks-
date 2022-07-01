from email.mime import image
import cv2

def main():
    image_path='./input_image/cmyk_paint.png'
    image=cv2.imread(image_path)
    
    cv2.imshow("Original",image)
    cv2.waitKey(0)
    
    B,G,R=cv2.split(image)
    
    cv2.imshow("Blue",B)
    cv2.waitKey(0)
    
    cv2.imshow("Green",G)
    cv2.waitKey(0)
    
    cv2.imshow("Red",R)
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
if __name__=='__main__':
    main()