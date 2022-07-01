from email.mime import image
import cv2

def main():
    image_path='./input_image/cmyk_paint.png'
    image=cv2.imread(image_path)
    
    cv2.imshow("Original",image)
    cv2.waitKey(0)
    
    B,G,R=cv2.split(image)
    
    cv2.imshow("Blue",B)
    #cv2.imwrite("./output_image/4.Blue.jpg")
    cv2.waitKey(0)
    
    cv2.imshow("Green",G)
    #cv2.imwrite("./output_image/4.Green.jpg")
    cv2.waitKey(0)
    
    cv2.imshow("Red",R)
    #cv2.imwrite("./output_image/4.Red.jpg")
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    
if __name__=='__main__':
    main()