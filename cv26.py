import cv2
import numpy as np

def sharpen_image(image):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image
image = cv2.imread('C:/Users/Admin/Downloads/craiyon_084318_Cartoon_drawing_of_a_cute_panda.png')
if image is None:
    print('Error: Unable to load image.')
else:
    sharpened_image = sharpen_image(image)
    cv2.imshow('Original Image', image)
    cv2.imshow('Sharpened Image', sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
