import cv2
import os

# Path to the image folder
img_folder = 'img_sample'
img_name = 'bird-sample.jpg'
img_path = os.path.join(img_folder, img_name)

# Load the image
image = cv2.imread(img_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Unable to load image at {img_path}")
else:
    # Display the image
    cv2.imshow('Sample Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()