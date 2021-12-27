import cv2

#reading image
img = cv2.imread('pencil_sketch.png')

#converting BGR image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#image inversion
inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("Original Image", img)
cv2.imshow("Pencil Sketch of Flower", pencil_sketch)
cv2.waitKey(0)
