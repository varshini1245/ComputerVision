import cv2
import numpy as np
def sharpen_image(image, k=1.5):
    kernel = np.array([[0, -1, 0],
                       [-1, k, -1],
                       [0, -1, 0]], dtype=np.float32)
    sharpened = cv2.filter2D(image, -1, kernel)
    high_boost = cv2.addWeighted(image, 1, sharpened, -0.5, 0)
    return high_boost
image = cv2.imread('C:/Users/Admin/Downloads/craiyon_084318_Cartoon_drawing_of_a_cute_panda.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sharpened_image = sharpen_image(gray_image)
cv2.imshow('Original Image', gray_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
