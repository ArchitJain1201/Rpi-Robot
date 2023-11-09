import customtkinter as ctk
import tkinter as tk
from presentation.UseCase import UseCase

from presentation.view.commonWidget.ArrowButton import ArrowButton

class MovementButton(tk.Frame):
    def __init__(self, master,use_case, bg="white",**kwargs):
        super().__init__(master, bg="white",**kwargs)

        self.use_case = use_case
            
        zoom =1
        subSample=1
        
        self.up_button = ArrowButton(self, "up",zoom=zoom,subSample=subSample, command=lambda event=None: self.use_case.button_callback_m("Up"))
        self.down_button = ArrowButton(self, "down",zoom=zoom,subSample=subSample, command=lambda event=None: self.use_case.button_callback_m("Down"))
        self.left_button = ArrowButton(self, "left",zoom=zoom,subSample=subSample, command=lambda event=None: UseCase.button_callback(button_name="Left"))
        self.right_button = ArrowButton(self, "right",zoom=zoom,subSample=subSample, command=lambda event=None: UseCase.button_callback(button_name="Right"))

        self.up_button.grid(row=0, column=1)
        self.down_button.grid(row=2, column=1)
        self.left_button.grid(row=1, column=0)
        self.right_button.grid(row=1, column=2)