import numpy as np
import cv2

img = cv2.imread('Lab1\peppers_color.jpg', 1)    
greyimg = np.zeros((img.shape[0], img.shape[1]), dtype = np.uint8)

# turn color image into grey image
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        greyimg[i][j] = (0.45 * img[i][j][0] + 0.35 * img[i][j][1] + 0.20 * img[i][j][2])

cv2.imwrite('Lab1\peppers_grey.jpg', greyimg)
cv2.imshow('peppers_grey', greyimg)
cv2.waitKey(0)
