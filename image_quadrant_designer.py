"""
This Python Code is completely designed for educational purposes.
This Python Code is used to change the image pixels quadrant wise.

I have used the .jpg format of the image in this program


"""


# These are python libraries...
import cv2
import numpy as np

# This function is to get the image name 
def get_image():
    image=input("Enter Image Name : ")
    return image

# This function is to change the image dimensions into n x n or n x m dimensions where n and m are even
def image_resize():
    name=f"{get_image()}"
    img=cv2.imread(f"{name}.jpg")
    d=cv2.resize(img,(256,256))
    cv2.imwrite("image_resized.jpg",d)

# This function is to divide into 4 equal parts   
def image_divider():
    img=cv2.imread(f"image_resized.jpg")
    h,w,channels=img.shape
    half=h//2
    half1=w//2
    up=img[:half,:]
    down=img[half:,:]  
    left_up=up[:,:half1]
    left_down=down[:,:half1]
    right_up=up[:,half1:]
    right_down=down[:,half1:]
    cv2.imwrite(f"right_up.jpg",right_up)
    cv2.imwrite(f"right_down.jpg",right_down)
    cv2.imwrite(f"left_up.jpg",left_up)
    cv2.imwrite(f"left_down.jpg",left_down)


# This function ist to change the image changer
def image_changer():
    right_up_image=cv2.imread("right_up.jpg")
    right_down_image=cv2.imread("right_down.jpg")
    left_down_image=cv2.imread("left_down.jpg")
    red=right_up_image[:,:,2]
    red_replacer=np.zeros(right_up_image.shape)
    red_replacer[:,:,2]=red
    green=right_down_image[:,:,1]
    green_replacer=np.zeros(right_down_image.shape)
    green_replacer[:,:,1]=green
    blue=left_down_image[:,:,0]
    blue_replacer=np.zeros(left_down_image.shape)
    blue_replacer[:,:,0]=blue
    cv2.imwrite("red_image.jpg",red_replacer)
    cv2.imwrite("green_image.jpg",green_replacer)
    cv2.imwrite("blue_image.jpg",blue_replacer)

# This function is to join the image parts

def image_joiner():
    right_up=cv2.imread("red_image.jpg")
    right_down=cv2.imread("green_image.jpg")
    left_up=cv2.imread("left_up.jpg")
    left_down=cv2.imread("blue_image.jpg")
    horizontal_join1=cv2.hconcat([left_up,right_up])
    horizontal_join2=cv2.hconcat([left_down,right_down])
    vertical_join=cv2.vconcat([horizontal_join1,horizontal_join2])
    cv2.imwrite("final_image.jpg",vertical_join)


# This Function is the combination of the two functions image_divider and image_chnager
# So we can write only this function in replacement of the two functions image_divider and image_chnager
def image_divider_changer():
    img=cv2.imread(f"image_resized.jpg")
    h,w,channels=img.shape
    half=h//2
    half1=w//2
    up=img[:half,:]
    down=img[half:,:]  
    left_up=up[:,:half1]
    left_down=down[:,:half1]
    right_up=up[:,half1:]
    right_down=down[:,half1:]
    red=right_up[:,:,2]
    red_replacer=np.zeros(right_up.shape)
    red_replacer[:,:,2]=red
    green=right_down[:,:,1]
    green_replacer=np.zeros(right_down.shape)
    green_replacer[:,:,1]=green
    blue=left_down[:,:,0]
    blue_replacer=np.zeros(left_down.shape)
    blue_replacer[:,:,0]=blue    
    cv2.imwrite(f"right_up1.jpg",red_replacer)
    cv2.imwrite(f"right_down1.jpg",green_replacer)
    cv2.imwrite(f"left_up1.jpg",left_up)
    cv2.imwrite(f"left_down1.jpg",blue_replacer)


image_resize()

image_divider()
image_changer()
# image_divider_changer() # This function will be called if we use the function...
image_joiner()