import cv2 as cv
import numpy as np

# 1 blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 2 point the image a certain color
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)

# 3 draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

cv.waitKey(0)