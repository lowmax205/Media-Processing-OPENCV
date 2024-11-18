import cv2
from tkinter import filedialog, messagebox, ttk
import customtkinter as ctk


def process_image(file_path):
    image = cv2.imread(file_path)
    if image is None:
        messagebox.showerror("Error", f"Unable to load the image: {file_path}")
    else:
        cv2.imshow("Processed Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def process_video(file_path):
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened():
        messagebox.showerror("Error", f"Unable to load the video: {file_path}")
    else:
        while cap.isOpened():
            ret, frame = cap.read()
            # if not ret:
            #     break
            cv2.imshow("Processed Video", frame)
            if cv2.waitKey(25) & 0xFF == ord("d"):
                break
        cap.release()
        cv2.destroyAllWindows()


def upload_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.configure(text=f"File selected: {file_path}")
    else:
        file_label.configure(text="No file selected")


def process():
    if file_path:
        if option_var.get() == "Image":
            process_image(file_path)
        elif option_var.get() == "Video":
            process_video(file_path)
    else:
        messagebox.showerror("Error", "No file selected")


BUTTON_WIDTH = 300

app = ctk.CTk()
app.title("Object Image Processing")

file_label = ctk.CTkLabel(app, text="No file selected", width=BUTTON_WIDTH)
file_label.pack(pady=10, padx=10)

option_var = ctk.StringVar(value="Image")
option_menu = ctk.CTkOptionMenu(
    app, variable=option_var, values=["Image", "Video"], width=BUTTON_WIDTH
)
option_menu.pack(pady=10)

upload_button = ctk.CTkButton(
    app, text="Upload Files", command=upload_file, width=BUTTON_WIDTH
)
upload_button.pack(pady=10)

process_button = ctk.CTkButton(app, text="Process", command=process, width=BUTTON_WIDTH)
process_button.pack(pady=10)

app.mainloop()
