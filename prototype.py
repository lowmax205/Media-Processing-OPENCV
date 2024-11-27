import cv2 as cv
import numpy as np

# 1 blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('#1 Blank', blank)

# 2 point the image a certain color
blank[200:300, 300:400] = 0,0,255
cv.imshow('#2 Red', blank)

# 3 draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow('#3 Rectangle Blue', blank)

# 4 draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,0,0), thickness=-1)
cv.imshow('#4 Circle Green', blank)

# 5 draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=1)
cv.imshow('#5 Line White', blank)

cv.waitKey(0)

