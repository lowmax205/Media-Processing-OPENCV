import cv2 as cv
import numpy as np


class BASIC:

    def basic_functions(
        img, dimensions=None, function=None, i=1, crop_coords=None, kernel_size=None
    ):
        if kernel_size is None:
            kernel_size = (1, 1)

        # Read in an image as a default img
        if img is None:
            # Read in an image
            img = cv.imread("sample_file/bird-sample.jpg")
            cv.imshow("Park", img)

        if function == "gray":
            # Converting to grayscale
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            cv.imshow("Gray", gray)

        elif function == "blur":
            # Blur
            blur = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)
            cv.imshow("Blur", blur)

        elif function == "canny":
            # Edge Cascade
            canny = cv.Canny(img, 125, 175)
            cv.imshow("Canny", canny)

        elif function == "dilate":
            # Dilating the image
            canny = cv.Canny(img, 125, 175)
            dilated = cv.dilate(canny, kernel_size, iterations=i)
            cv.imshow("Dilated", dilated)

        elif function == "erode":
            # Eroding
            canny = cv.Canny(img, 125, 175)
            dilated = cv.dilate(canny, kernel_size, iterations=i)
            eroded = cv.erode(dilated, kernel_size, iterations=i)
            cv.imshow("Eroded", eroded)

        elif function == "resize":
            if dimensions is None:
                dimensions = (300, 300)  # Default dimensions
            # Resize
            resized = cv.resize(img, dimensions, interpolation=cv.INTER_CUBIC)
            cv.imshow("Resized", resized)

        elif function == "crop":
            # Cropping
            if crop_coords is None:
                crop_coords = (50, 200, 200, 400)  # Default coordinates
            y1, y2, x1, x2 = crop_coords
            cropped = img[y1:y2, x1:x2]
            cv.imshow("Cropped", cropped)
        else:
            print("Invalid Basic function")

    def read_functions(video_path=None):

        # Reading in a video
        if video_path is None:
            video_path = "sample_file/video_sample.mp4"
        capture = cv.VideoCapture(video_path)

        while True:
            isTrue, frame = capture.read()

            if isTrue:
                cv.imshow("Video", frame)
                if cv.waitKey(20) & 0xFF == ord("d"):
                    break
            else:
                break

        capture.release()
        cv.destroyAllWindows()

    def draw_functions(
        img,
        function,
        color=None,
        thickness=None,
        start_point=None,
        end_point=None,
        radius=None,
        text=None,
        position=None,
    ):
        if color is None:
            color = (0, 0, 255)
        if thickness is None:
            thickness = 2

        if function == "rectangle":
            if start_point is None:
                start_point = (0, 0)
            if end_point is None:
                end_point = (250, 350)
            # Drawing a rectangle
            rectangle = cv.rectangle(img, start_point, end_point, color, thickness)
            cv.imshow("Rectangle", rectangle)

        elif function == "circle":
            if start_point is None:
                start_point = (400, 50)
            if radius is None:
                radius = 30
            # Drawing a circle
            circle = cv.circle(img, start_point, radius, color, thickness)
            cv.imshow("Circle", circle)

        elif function == "line":
            if start_point is None:
                start_point = (100, 250)
            if end_point is None:
                end_point = (300, 400)
            # Drawing a line
            line = cv.line(img, start_point, end_point, color, thickness)
            cv.imshow("Line", line)

        elif function == "text":
            if text is None:
                text = "OpenCV Text Function"
            if position is None:
                position = (300, 100)
            # Adding text
            text_img = cv.putText(
                img,
                text,
                position,
                cv.FONT_HERSHEY_COMPLEX,
                1.0,
                color,
                thickness,
            )
            cv.imshow("Text", text_img)

        elif function == "paint":
            # Paint the image a certain color
            painted_img = img.copy()
            painted_img[:] = color
            cv.imshow("Paint", painted_img)
        else:
            print("Invalid Draw function")

    def transformations(
        img,
        function,
        x=None,
        y=None,
        angle=None,
        rotPoint=None,
        flipCode=None,
        crop_coords=None,
    ):
        if function == "translate":
            # Translation
            transMat = np.float32([[1, 0, x], [0, 1, y]])
            dimensions = (img.shape[1], img.shape[0])
            translated = cv.warpAffine(img, transMat, dimensions)
            cv.imshow("Translated", translated)

        elif function == "rotate":
            # Rotation
            (height, width) = img.shape[:2]
            if rotPoint is None:
                rotPoint = (width // 2, height // 2)
            rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
            dimensions = (width, height)
            rotated = cv.warpAffine(img, rotMat, dimensions)
            cv.imshow("Rotated", rotated)

        elif function == "flip":
            # Flipping
            flipped = cv.flip(img, flipCode)
            cv.imshow("Flipped", flipped)

        elif function == "crop":
            # Cropping
            y1, y2, x1, x2 = crop_coords
            cropped = img[y1:y2, x1:x2]
            cv.imshow("Cropped", cropped)
        else:
            print("Invalid Transformation function")

    def thresh(
        img_path=None,
        function=None,
        reverse=False,
        simple_thresh_val=150,
        max_val=255,
        adaptive_method=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
        adaptive_thresh_type=cv.THRESH_BINARY_INV,
        block_size=11,
        C=9,
    ):
        if img_path is None:
            img_path = "sample_file/bird-sample.jpg"
            img = cv.imread(img_path)
            cv.imshow("Cats", img)

        if function == "thresh":
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            cv.imshow("Gray", gray)

        elif function == "thresh":

            if reverse is not True:
                # Simple Thresholding
                threshold, thresh = cv.threshold(
                    gray, simple_thresh_val, max_val, cv.THRESH_BINARY
                )
                cv.imshow("Simple Thresholded", thresh)
            else:
                threshold, thresh_inv = cv.threshold(
                    gray, simple_thresh_val, max_val, cv.THRESH_BINARY_INV
                )
                cv.imshow("Simple Thresholded Inverse", thresh_inv)
        elif function == "adaptive":
            # Adaptive Thresholding
            adaptive_thresh = cv.adaptiveThreshold(
                gray, max_val, adaptive_method, adaptive_thresh_type, block_size, C
            )
            cv.imshow("Adaptive Thresholding", adaptive_thresh)
        else:
            print("Invalid Threshold function")

    def contours(img_path=None, function=None, canny_thresh1=None, canny_thresh2=None):
        if img_path is None:
            img_path = "sample_file/bird-sample.jpg"

        if canny_thresh1 or canny_thresh2 is None:
            canny_thresh1 = 125
            canny_thresh2 = 175

        if function == "read_image":

            img = cv.imread(img_path)
            cv.imshow("Cats", img)
        elif function == "blank_image":
            blank = np.zeros(img.shape, dtype="uint8")
            cv.imshow("Blank", blank)
        elif function == "gray_color":
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            cv.imshow("Gray", gray)
        elif function == "blur":
            blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
            cv.imshow("Blur", blur)
        elif function == "Canny_edges":

            canny = cv.Canny(blur, canny_thresh1, canny_thresh2)
            cv.imshow("Canny Edges", canny)
        elif function == "contours":
            contours, hierarchies = cv.findContours(
                canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE
            )
            print(f"{len(contours)} contour(s) found!")

            cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
            cv.imshow("Contours Drawn", blank)

        cv.waitKey(0)

    @staticmethod
    def get_functions():
        return {
            "basic_functions": [
                "gray",
                "blur",
                "canny",
                "dilate",
                "erode",
                "resize",
                "crop",
            ],
            "draw_functions": ["rectangle", "circle", "line", "text", "paint"],
            "transformations": ["translate", "rotate", "flip", "crop"],
            "thresh": ["thresh", "adaptive"],
            "contours": [
                "read_image",
                "blank_image",
                "gray_color",
                "blur",
                "Canny_edges",
                "contours",
            ],
        }
