import cv2 as cv
import numpy as np

class basic_functions:
    
    def functions(img, dimensions, function, i, crop_coords=None, kernel_size=None):
        if kernel_size is None:
            kernel_size = (7,7)
        
        # Read in an image as a default img
        if img is None:
            # Read in an image
            img = cv.imread('sample_file/bird-sample.jpg')
            cv.imshow('Park', img)

        if function == 'gray':
            # Converting to grayscale
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            cv.imshow('Gray', gray)

        elif function == 'blur':
            # Blur 
            blur = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)
            cv.imshow('Blur', blur)

        elif function == 'canny':
            # Edge Cascade
            canny = cv.Canny(img, 125, 175)
            cv.imshow('Canny', canny)

        elif function == 'dilate':
            # Dilating the image
            canny = cv.Canny(img, 125, 175)
            dilated = cv.dilate(canny, kernel_size, iterations=i)
            cv.imshow('Dilated', dilated)

        elif function == 'erode':
            # Eroding
            canny = cv.Canny(img, 125, 175)
            dilated = cv.dilate(canny, kernel_size, iterations=i)
            eroded = cv.erode(dilated, kernel_size, iterations=i)
            cv.imshow('Eroded', eroded)

        elif function == 'resize':
            # Resize
            resized = cv.resize(img, dimensions, interpolation=cv.INTER_CUBIC)
            cv.imshow('Resized', resized)

        elif function == 'crop':
            # Cropping
            if crop_coords is None:
                crop_coords = (50, 200, 200, 400)  # Default coordinates
            y1, y2, x1, x2 = crop_coords
            cropped = img[y1:y2, x1:x2]
            cv.imshow('Cropped', cropped)
class read_functions:
    def functions(video_path=None):

        # Reading in a video
        if video_path is None:
            video_path = 'sample_file/video_sample.mp4'
        capture = cv.VideoCapture(video_path)

        while True:
            isTrue, frame = capture.read()

            if isTrue:
                cv.imshow('Video', frame)
                if cv.waitKey(20) & 0xFF==ord('d'):
                    break
            else:
                break

        capture.release()
        cv.destroyAllWindows()        
class draw_functions:
        
        def functions(img, function, color=None, thickness=None):
            if color is None:
                color = (0, 0, 255)
            if thickness is None:
                thickness = 2
            
            if function == 'rectangle':
                # Drawing a rectangle
                cv.rectangle(img, (0, 0), (250, 350), color, thickness)
                cv.imshow('Rectangle', img)
    
            elif function == 'circle':
                # Drawing a circle
                cv.circle(img, (400, 50), 30, color, thickness)
                cv.imshow('Circle', img)
    
            elif function == 'line':
                # Drawing a line
                cv.line(img, (100, 250), (300, 400), color, thickness)
                cv.imshow('Line', img)
    
            elif function == 'text':
                # Adding text
                cv.putText(img, 'OpenCV Text Function', (300, 100), cv.FONT_HERSHEY_COMPLEX, 1.0, color, thickness)
                cv.imshow('Text', img)

            elif function == 'paint':
                # Paint the image a certain color
                img[:] = color
                cv.imshow('Paint', img)
                
class transformations:
    def functions(img, x=None, y=None, angle=None, rotPoint=None, flipCode=None, crop_coords=None):
        if x is not None and y is not None:
            # Translation
            transMat = np.float32([[1,0,x],[0,1,y]])
            dimensions = (img.shape[1], img.shape[0])
            translated = cv.warpAffine(img, transMat, dimensions)
            cv.imshow('Translated', translated)

        if angle is not None:
            # Rotation
            (height, width) = img.shape[:2]
            if rotPoint is None:
                rotPoint = (width//2, height//2)
            rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
            dimensions = (width, height)
            rotated = cv.warpAffine(img, rotMat, dimensions)
            cv.imshow('Rotated', rotated)

        if flipCode is not None:
            # Flipping
            flipped = cv.flip(img, flipCode)
            cv.imshow('Flipped', flipped)

        if crop_coords is not None:
            # Cropping
            y1, y2, x1, x2 = crop_coords
            cropped = img[y1:y2, x1:x2]
            cv.imshow('Cropped', cropped)

class thresh:
    def functions(img_path=None, simple_thresh_val=150, max_val=255, adaptive_method=cv.ADAPTIVE_THRESH_GAUSSIAN_C, adaptive_thresh_type=cv.THRESH_BINARY_INV, block_size=11, C=9):
        if img_path is None:
            img_path = 'sample_file/bird-sample.jpg'
        img = cv.imread(img_path)
        cv.imshow('Cats', img)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('Gray', gray)
        
        # Simple Thresholding
        threshold, thresh = cv.threshold(gray, simple_thresh_val, max_val, cv.THRESH_BINARY)
        cv.imshow('Simple Thresholded', thresh)

        threshold, thresh_inv = cv.threshold(gray, simple_thresh_val, max_val, cv.THRESH_BINARY_INV)
        cv.imshow('Simple Thresholded Inverse', thresh_inv)

        # Adaptive Thresholding
        adaptive_thresh = cv.adaptiveThreshold(gray, max_val, adaptive_method, adaptive_thresh_type, block_size, C)
        cv.imshow('Adaptive Thresholding', adaptive_thresh)
        
class contours:
    def functions(img_path=None, canny_thresh1=None, canny_thresh2=None):
        if img_path is None:
            img_path = 'sample_file/bird-sample.jpg'
            
        if canny_thresh1 or canny_thresh2 is None:
            canny_thresh1 = 125
            canny_thresh2 = 175
        img = cv.imread(img_path)

        img = cv.imread(img_path)
        cv.imshow('Cats', img)

        blank = np.zeros(img.shape, dtype='uint8')
        cv.imshow('Blank', blank)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('Gray', gray)

        blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
        cv.imshow('Blur', blur)

        canny = cv.Canny(blur, canny_thresh1, canny_thresh2)
        cv.imshow('Canny Edges', canny)

        contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        print(f'{len(contours)} contour(s) found!')

        cv.drawContours(blank, contours, -1, (0,0,255), 1)
        cv.imshow('Contours Drawn', blank)

        cv.waitKey(0)