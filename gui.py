from tkinter import filedialog, messagebox
import customtkinter as ctk
from typing import Optional
from media_processor import MediaProcessor


class ImageProcessingApp:
    BUTTON_WIDTH = 300

    def __init__(self):
        self.file_path: Optional[str] = None
        self.app = ctk.CTk()
        self.app.title("Object Image Processing")
        self.processor = MediaProcessor()
        self._create_widgets()

    def _create_widgets(self):
        self.file_label = ctk.CTkLabel(
            self.app,
            text="No file selected",
            width=self.BUTTON_WIDTH,
            wraplength=self.BUTTON_WIDTH - 20,
        )
        self.file_label.pack(pady=10, padx=10)

        self.option_var = ctk.StringVar(value="Image")
        self.option_menu = ctk.CTkOptionMenu(
            self.app,
            variable=self.option_var,
            values=["Image", "Video", "Webcam"],
            width=self.BUTTON_WIDTH,
            command=self._on_file_type_change,
        )
        self.option_menu.pack(pady=10)

        self.upload_button = ctk.CTkButton(
            self.app,
            text="Upload Files",
            command=self._upload_file,
            width=self.BUTTON_WIDTH,
        )
        self.upload_button.pack(pady=10)

        self.process_button = ctk.CTkButton(
            self.app, text="Process", command=self._process, width=self.BUTTON_WIDTH
        )
        self.process_button.pack(pady=10)

    def _on_file_type_change(self, _):
        self.file_path = None
        self.file_label.configure(text="No file selected")
        self.upload_button.configure(state="normal")

    def _upload_file(self):
        if self.option_var.get() == "Webcam":
            self.file_path = filedialog.askdirectory(title="Select Sample Folder")
            if self.file_path:
                self.file_label.configure(
                    text=f"Sample folder selected: {self.file_path}"
                )
                self.upload_button.configure(state="disabled")
            else:
                self.file_label.configure(text="No sample folder selected")
        else:
            filetypes = (
                [("Images", "*.jpg;*.jpeg;*.png")]
                if self.option_var.get() == "Image"
                else [("Videos", "*.mp4;*.avi")]
            )
            self.file_path = filedialog.askopenfilename(filetypes=filetypes)
            if self.file_path:
                self.file_label.configure(text=f"File selected: {self.file_path}")
                self.upload_button.configure(state="disabled")
            else:
                self.file_label.configure(text="No file selected")

    def _process(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected")
            return

        try:
            if self.option_var.get() == "Image":
                self.processor.process_image(self.file_path)
            elif self.option_var.get() == "Video":
                self.processor.process_video(self.file_path)
            else:
                self.processor.process_webcam(self.file_path)
            self.upload_button.configure(state="normal")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.upload_button.configure(state="normal")

    def run(self):
        self.app.mainloop()
