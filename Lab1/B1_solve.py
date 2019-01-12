import numpy as np 
import cv2 

img = cv2.imread('Lab1/cameraman.png',0)
rgbimg = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

# turn grey image into color image
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i][j] >= 0 and img[i][j] <= 100:
            rgbimg[i][j][0] = 0
            rgbimg[i][j][1] = 0
            rgbimg[i][j][2] = 255
        elif img[i][j] >= 101 and img[i][j] <= 200:
            rgbimg[i][j][0] = 0
            rgbimg[i][j][1] = 255
            rgbimg[i][j][2] = 0
        else: 
            rgbimg[i][j][0] = 255
            rgbimg[i][j][1] = 0
            rgbimg[i][j][2] = 0

cv2.imwrite('Lab1/cameramancolor.jpg', rgbimg)
cv2.imshow('image', rgbimg)
cv2.waitKey(0)

