import cv2
path = r"C:/Users/Admin/Pictures/craiyon_084318_Cartoon_drawing_of_a_cute_panda.jpg"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
