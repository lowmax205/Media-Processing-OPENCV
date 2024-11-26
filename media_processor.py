import cv2
import os


class basic_image_processing:

    # Reading Images & Video
    # 1 Image Reading
    @staticmethod
    def process_image(
        file_path: str,
        should_rescale=False,
        scale=None,
        should_resize=False,
        width=None,
        height=None,
    ) -> None:
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError(f"Unable to load the image: {file_path}")
        image = basic_image_processing.resize_or_rescale_frame(
            image, should_rescale, scale, should_resize, width, height
        )
        cv2.imshow("Processed Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 2 Reading Videos
    @staticmethod
    def process_video(
        file_path: str,
        should_rescale=False,
        scale=None,
        should_resize=False,
        width=None,
        height=None,
    ) -> None:
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            raise ValueError(f"Unable to load the video: {file_path}")
        # Part of Resize functionality
        if should_resize and width and height:
            cap.set(3, width)
            cap.set(4, height)
        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frame = basic_image_processing.resize_or_rescale_frame(
                    frame, should_rescale, scale, should_resize, width, height
                )
                cv2.imshow("Processed Video", frame)
                if cv2.waitKey(20) & 0xFF == ord("d"):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()

    # Resizing and Rescaling Frames
    @staticmethod
    def resize_or_rescale_frame(
        frame,
        should_rescale=False,
        scale=None,
        should_resize=False,
        width=None,
        height=None,
    ):
        if should_rescale:
            frame = basic_image_processing.rescale_frame(frame, scale)
        if should_resize and width and height:
            frame = basic_image_processing.resize_frame(frame, width, height)
        return frame

    # 3 Rescale
    @staticmethod
    def rescale_frame(frame, scale: float = 0.50):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

    # 4 Resize
    @staticmethod
    def resize_frame(frame, width, height):
        return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

    # Webcam Processing
    @staticmethod
    def process_webcam(img_sample_folder: str) -> None:
        if not os.path.exists(img_sample_folder):
            raise ValueError(f"Sample folder does not exist: {img_sample_folder}")

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise ValueError("Unable to access the webcam")

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = basic_image_processing.rescale_frame(frame)
                # Add object recognition logic here using img_sample_folder
                cv2.imshow("Webcam Feed", frame)
                if cv2.waitKey(20) & 0xFF == ord("q"):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()
