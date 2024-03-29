import cv2
import numpy as np
img = cv2.imread("C:/Users/Admin/Downloads/craiyon_084318_Cartoon_drawing_of_a_cute_panda.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Original", img)
cv2.imshow("Closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
