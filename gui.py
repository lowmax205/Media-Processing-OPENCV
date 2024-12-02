from tkinter import filedialog, messagebox, ttk
import customtkinter as ctk

class ProcessingGui:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Image Processing App")
        self.root.after(0, self.set_fullscreen)
    
    def set_fullscreen(self):
        self.root.state("zoomed")
    
    def run(self):
        self.root.mainloop()