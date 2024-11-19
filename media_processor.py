import cv2
import os


class MediaProcessor:
    @staticmethod
    def rescale_frame(frame, scale: float = 0.50):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

    @staticmethod
    def process_image(file_path: str) -> None:
        image = cv2.imread(file_path)
        if image is None:
            raise ValueError(f"Unable to load the image: {file_path}")
        image = MediaProcessor.rescale_frame(image)
        cv2.imshow("Processed Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def process_video(file_path: str) -> None:
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            raise ValueError(f"Unable to load the video: {file_path}")
        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                frame = MediaProcessor.rescale_frame(frame)
                cv2.imshow("Processed Video", frame)
                if cv2.waitKey(20) & 0xFF == ord("d"):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()

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
                frame = MediaProcessor.rescale_frame(frame)
                # Add object recognition logic here using img_sample_folder
                cv2.imshow("Webcam Feed", frame)
                if cv2.waitKey(20) & 0xFF == ord("q"):
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()
