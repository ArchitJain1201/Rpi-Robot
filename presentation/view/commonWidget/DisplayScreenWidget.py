import tkinter as tk
import customtkinter as ctk

class DisplayScreenWidget(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(expand=True, fill="both")

    def create_image(self, x, y, **kwargs):
        return self.canvas.create_image(x, y, **kwargs)
