import cv2 as cv
import numpy as np

WIDTH = 300
HEIGHT = 300

# Create a black image
blank = np.zeros((HEIGHT, WIDTH, 3), dtype="uint8")
cv.imshow("Blank", blank)

# 1. Paint the image a certain Colour
red = blank[:] = 0, 0, 255
cv.imshow("Red", red)

# 2. Draw a Rectangle
rectangle = cv.rectangle(
    blank,
    (0, 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (0, 255, 0),
    thickness=cv.FILLED,
)
cv.imshow("Green Rectangle", rectangle)

# 3. Draw a Circle
circle = cv.circle(
    blank,
    (blank.shape[1] // 2, blank.shape[0] // 2),
    40,
    (255, 0, 0),
    thickness=3,
)
cv.imshow("Blue Circle", circle)

# 4. Draw a Line
white_line = cv.line(
    blank,
    (0, 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (255, 255, 255),
    thickness=3,
)
cv.imshow("c Line", white_line)

# 5. Write Text
write_text = cv.putText(
    blank,
    "Hello, World",
    (0, blank.shape[0] // 2),
    cv.FONT_HERSHEY_TRIPLEX,
    1.0,
    (0, 255, 225),
    2,
)
cv.imshow("Yellow Text", write_text)

while True:
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()
