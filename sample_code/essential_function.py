import cv2 as cv

# Read an image with original image
img = cv.imread("img_sample/bird-sample.jpg")
cv.imshow("Sample", img)

# 1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

# 2. Blur the image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur Image", blur)

# 3. Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Image", canny)

# 4. Applying Blur to edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Image with Blur", canny)

# 5. Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated Image", dilated)

# 6. Eroding the image
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded Image", eroded)

# 7. Cropping the image
cropped = img[50:200, 200:400]

while True:
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()
