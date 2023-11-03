from tkinter import filedialog
import tkinter as tk
import serial
from PIL import Image,ImageTk

class UseCase:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def button_callback(button_name):
        print(f"{button_name} button pressed")

    def switch_display(self, x=10, y=10):
        if self.app.live_camera:
            self.app.switch_button.set_text("Switch to Gallery")
            # Switch to image from gallery
            file_path = filedialog.askopenfilename(title="Select an Image",filetypes=[("Image files", ("*.png", "*.jpg", "*.jpeg")), ("All files", "*.*")])
            if file_path:
                image = Image.open(file_path)
                img = image.resize((240,240))
                self.image = ImageTk.PhotoImage(img)
                self.displayImg = self.image
                self.app.display_screen.create_image(x, y, image=self.displayImg)
        else:
            self.app.switch_button.set_text("Switch to Live Camera")
            # Mock code for displaying camera input, replace with actual camera input code

        self.app.live_camera = not self.app.live_camera
    @staticmethod
    def send_serial_message(message, com_port='/dev/ttyUSB0', baud_rate=9600):
        try:
            with serial.Serial(com_port, baud_rate) as ser:
                ser.write(message.encode())
        except serial.SerialException as e:
            print(f"{e}")
        
