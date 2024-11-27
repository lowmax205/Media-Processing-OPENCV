from tkinter import filedialog, messagebox, ttk
import customtkinter as ctk
from typing import Optional
from media_processor import basic_image_processing


class ImageProcessingApp:
    BUTTON_WIDTH = 300

    def __init__(self):
        self.file_path: Optional[str] = None
        self.app = ctk.CTk()
        self.app.title("Object Image Processing")
        self.processor = basic_image_processing()
        self.should_rescale = ctk.BooleanVar(value=False)
        self.scale_value = ctk.StringVar(value="")
        self.should_resize = ctk.BooleanVar(value=False)
        self.width_value = ctk.StringVar(value="")
        self.height_value = ctk.StringVar(value="")
        self._create_widgets()

    def _create_widgets(self):
        self.app.grid_rowconfigure(4, weight=1)
        self.app.grid_columnconfigure((0, 1, 2), weight=1)

        self.file_label = ctk.CTkLabel(
            self.app,
            text="No file selected",
            width=self.BUTTON_WIDTH,
            wraplength=self.BUTTON_WIDTH - 20,
        )
        self.file_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        self.upload_button = ctk.CTkButton(
            self.app,
            text="Upload Files",
            command=self._upload_file,
            width=self.BUTTON_WIDTH,
        )
        self.upload_button.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

        self.process_button = ctk.CTkButton(
            self.app,
            text="Process",
            command=self._process,
            width=self.BUTTON_WIDTH,
            state="disabled",
        )
        self.process_button.grid(row=2, column=0, columnspan=3, pady=10, padx=10)

        self.basic_button = ctk.CTkButton(
            self.app, text="Basic", command=lambda: self.select_tab(self.basic_tab)
        )
        self.basic_button.grid(row=3, column=0, pady=10, padx=5)
        self.advanced_button = ctk.CTkButton(
            self.app,
            text="Advanced",
            command=lambda: self.select_tab(self.advanced_tab),
        )
        self.advanced_button.grid(row=3, column=1, pady=10, padx=5)
        self.faces_button = ctk.CTkButton(
            self.app, text="Faces", command=lambda: self.select_tab(self.faces_tab)
        )
        self.faces_button.grid(row=3, column=2, pady=10, padx=5)

        self.basic_tab = ctk.CTkFrame(self.app, fg_color=None, corner_radius=0)
        self.advanced_tab = ctk.CTkFrame(self.app, fg_color=None, corner_radius=0)
        self.faces_tab = ctk.CTkFrame(self.app, fg_color=None, corner_radius=0)

        self.all_tabs = [self.basic_tab, self.advanced_tab, self.faces_tab]
        for tab in self.all_tabs:
            tab.grid(
                row=4, column=0, columnspan=3, sticky="nsew"
            )

        self._create_basic_widgets()
        self._create_advanced_widgets()
        self._create_faces_widgets()

        self.select_tab(self.basic_tab)

    def select_tab(self, selected_tab: ctk.CTkFrame):
        selected_tab.grid(
            row=4, column=0, columnspan=3, sticky="nsew"
        )
        for tab in self.all_tabs:
            if tab is not selected_tab:
                tab.grid_forget()

    def _create_basic_widgets(self):
        self.option_var = ctk.StringVar(value="Image")
        self.option_menu = ctk.CTkOptionMenu(
            self.basic_tab,
            variable=self.option_var,
            values=["Image", "Video", "Webcam"],
            width=self.BUTTON_WIDTH,
            command=self._on_file_type_change,
        )
        self.option_menu.pack(pady=10)

        self.rescale_checkbox = ctk.CTkCheckBox(
            self.basic_tab,
            text="Rescale",
            variable=self.should_rescale,
            command=lambda: self._toggle_frame(self.should_rescale, self.scale_frame),
        )
        self.rescale_checkbox.pack(pady=5)
        self.scale_frame = ctk.CTkFrame(self.basic_tab)
        self.scale_label = ctk.CTkLabel(self.scale_frame, text="Rescale Factor ")
        self.scale_label.pack(side="top")
        self.scale_entry = ctk.CTkEntry(
            self.scale_frame,
            textvariable=self.scale_value,
            placeholder_text="Scale (e.g., 0.75)",
        )
        self.scale_entry.pack(side="left", pady=5, padx=5)
        self.scale_frame.pack(pady=5)
        self.scale_frame.pack_forget()

        self.resize_checkbox = ctk.CTkCheckBox(
            self.basic_tab,
            text="Resize",
            variable=self.should_resize,
            command=lambda: self._toggle_frame(self.should_resize, self.size_frame),
        )
        self.resize_checkbox.pack(pady=5)
        self.size_frame = ctk.CTkFrame(self.basic_tab)

        self.width_frame = ctk.CTkFrame(self.size_frame)
        self.width_label = ctk.CTkLabel(self.width_frame, text="Width ")
        self.width_label.pack(side="top")
        self.width_entry = ctk.CTkEntry(
            self.width_frame, textvariable=self.width_value, placeholder_text="Width"
        )
        self.width_entry.pack(side="top", pady=5, padx=5)
        self.width_frame.pack(side="left", padx=10, pady=10)

        self.height_frame = ctk.CTkFrame(self.size_frame)
        self.height_label = ctk.CTkLabel(self.height_frame, text="Height ")
        self.height_label.pack(side="top")
        self.height_entry = ctk.CTkEntry(
            self.height_frame, textvariable=self.height_value, placeholder_text="Height"
        )
        self.height_entry.pack(side="top", pady=5, padx=5)
        self.height_frame.pack(side="left", padx=10, pady=10)

        self.size_frame.pack(pady=10, padx=10)
        self.size_frame.pack_forget()

    def _toggle_frame(self, variable, frame):
        if variable.get():
            frame.pack(pady=5)
        else:
            frame.pack_forget()

    def _create_advanced_widgets(self):
        pass

    def _create_faces_widgets(self):
        pass

    def _on_file_type_change(self, _):
        self.file_path = None
        self.file_label.configure(text="No file selected")
        self.upload_button.configure(state="normal")
        self.process_button.configure(state="disabled")

    def _upload_file(self):
        if self.option_var.get() == "Webcam":
            self.file_path = filedialog.askdirectory(title="Select Sample Folder")
            if self.file_path:
                self.file_label.configure(
                    text=f"Sample folder selected: {self.file_path}"
                )
                self.upload_button.configure(state="disabled")
                self.process_button.configure(state="normal")
            else:
                self.file_label.configure(text="No sample folder selected")
                self.process_button.configure(state="disabled")
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
                self.process_button.configure(state="normal")
            else:
                self.file_label.configure(text="No file selected")
                self.process_button.configure(state="disabled")

    def _process(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected")
            return

        try:
            should_rescale = self.should_rescale.get()
            scale = float(self.scale_value.get()) if self.scale_value.get() else None
            should_resize = self.should_resize.get()
            width = int(self.width_value.get()) if self.width_value.get() else None
            height = int(self.height_value.get()) if self.height_value.get() else None

            if self.option_var.get() == "Image":
                self.processor.process_image(
                    self.file_path, should_rescale, scale, should_resize, width, height
                )
            elif self.option_var.get() == "Video":
                self.processor.process_video(
                    self.file_path, should_rescale, scale, should_resize, width, height
                )
            else:
                self.processor.process_webcam(self.file_path, scale)
            self.upload_button.configure(state="normal")
            self.process_button.configure(state="disabled")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.upload_button.configure(state="normal")

    def run(self):
        self.app.mainloop()
