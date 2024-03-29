import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('C:\\Users\\ASUS\\Pictures\\Camera Roll\\WIN_20240326_14_26_39_Pro.jpg', 0)  # Load the image in grayscale mode

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Display original and equalized image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')

plt.show()
