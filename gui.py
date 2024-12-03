from tkinter import filedialog, messagebox, ttk
import customtkinter as ctk
from media_processor import section1
import cv2 as cv
from PIL import Image, ImageTk


class ProcessingGui:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Image Processing App")
        self.root.after(0, self.set_fullscreen)

        self.functions = section1.get_functions()
        self.selected_function = ctk.StringVar()
        self.selected_subfunction = ctk.StringVar()
        self.file_path = None

        self.create_widgets()

    def set_fullscreen(self):
        self.root.state("zoomed")

    def create_widgets(self):
        left_frame = ctk.CTkFrame(self.root)
        left_frame.pack(side="left", fill="y", padx=10, pady=10)

        function_label = ctk.CTkLabel(left_frame, text="Select Function:")
        function_label.pack(pady=10)

        function_dropdown = ctk.CTkOptionMenu(
            left_frame,
            variable=self.selected_function,
            values=list(self.functions.keys()),
            command=self.update_subfunctions,
        )
        function_dropdown.pack(pady=10)

        self.subfunction_dropdown = ctk.CTkOptionMenu(
            left_frame, variable=self.selected_subfunction, values=[]
        )
        self.subfunction_dropdown.pack(pady=10)

        upload_button = ctk.CTkButton(
            left_frame, text="Upload File", command=self.upload_file
        )
        upload_button.pack(pady=10)

        self.process_button = ctk.CTkButton(
            left_frame, text="Process", command=self.process_function
        )
        self.process_button.pack(pady=10)

        self.canvas = ctk.CTkCanvas(self.root, width=800, height=600)
        self.canvas.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.crop_coords_entry = ctk.CTkEntry(
            left_frame, placeholder_text="Crop Coords (y1,y2,x1,x2)"
        )
        self.kernel_size_entry = ctk.CTkEntry(
            left_frame, placeholder_text="Kernel Size (k1,k2)"
        )
        self.dimensions_entry = ctk.CTkEntry(
            left_frame, placeholder_text="Dimensions (w,h)"
        )

    def update_subfunctions(self, selected_function):
        subfunctions = self.functions[selected_function]
        self.subfunction_dropdown.configure(values=subfunctions)
        self.selected_subfunction.set(subfunctions[0])

        if selected_function == "basic_functions":
            self.crop_coords_entry.pack(pady=10)
            self.kernel_size_entry.pack(pady=10)
            self.dimensions_entry.pack(pady=10)
        else:
            self.crop_coords_entry.pack_forget()
            self.kernel_size_entry.pack_forget()
            self.dimensions_entry.pack_forget()

    def upload_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            messagebox.showinfo("File Selected", f"Selected file: {self.file_path}")

    def process_function(self):
        selected_function = self.selected_function.get()
        selected_subfunction = self.selected_subfunction.get()
        print(
            f"Processing {selected_function} with {selected_subfunction} on file {self.file_path}"
        )

        if self.file_path:
            img = cv.imread(self.file_path)
            if selected_function == "basic_functions":
                crop_coords = self.parse_entry(self.crop_coords_entry.get())
                kernel_size = self.parse_entry(self.kernel_size_entry.get())
                dimensions = self.parse_entry(self.dimensions_entry.get())
                section1.basic_functions(
                    img,
                    dimensions,
                    selected_subfunction,
                    crop_coords=crop_coords,
                    kernel_size=kernel_size,
                )
            else:
                self.display_image_on_canvas(img)

    def parse_entry(self, entry):
        if entry:
            return tuple(map(int, entry.split(",")))
        return None

    def display_image_on_canvas(self, img):
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        self.canvas.create_image(0, 0, anchor="nw", image=img_tk)
        self.canvas.image = img_tk

    def run(self):
        self.root.mainloop()
