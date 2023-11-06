from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os

class UseCase:
    def __init__(self, app):
        self.app = app
        self.image_paths = []
        self.current_image_index = 0

    @staticmethod
    def button_callback(button_name):
        print(f"{button_name} button pressed")

    def update_image_display(self):

        # Get the actual dimensions of the display screen
        self.app.root.update()  # This ensures the window is updated
        screen_height = self.app.display_screen.winfo_height()

        # Open the image
        image = Image.open(self.image_paths[self.current_image_index])

        # Calculate the new width maintaining the aspect ratio
        aspect_ratio = image.width / image.height
        new_width = int(screen_height * aspect_ratio)

        # Resize the image to fit the y-axis of the screen
        #image = image.resize((new_width, screen_height), Image.Resampling.LANCZOS)
        image = image.resize((new_width, screen_height), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image)

        # Calculate position to center the image on the screen
        screen_width = self.app.display_screen.winfo_width()
        x_position = screen_width // 2

        # Create image in the center of the canvas
        self.app.display_screen.create_image(x_position, screen_height // 2, image=self.image, anchor="center")

    def switch_display(self, x=1000, y=1000):
        if self.app.live_camera:
            self.app.switch_button.set_text("Switch to Gallery")
            # Switch to image from gallery
            self.image_paths= filedialog.askopenfilename(title="Select an Image",filetypes=[("Image files", ("*.png", "*.jpg", "*.jpeg")), ("All files", "*.*")])
            self.current_image_index = 0
            if self.image_paths:
                self.update_image_display()

        else:
            self.app.switch_button.set_text("Switch to Live Camera")
            # Mock code for displaying camera input, replace with actual camera input code

        self.app.live_camera = not self.app.live_camera

    def next_image(self):
        if not self.app.live_camera and self.image_paths:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.update_image_display()

    def previous_image(self):
        if not self.app.live_camera and self.image_paths:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.update_image_display()

    @staticmethod
    def button_callback(app,button_name):
        if app.live_camera:  # Assuming 'app' is accessible here, or pass it as an argument
            print(f"{button_name} button pressed")
        else:
            if button_name == "Up":
                app.use_case.previous_image()
            elif button_name == "Down":
                app.use_case.next_image()
            # No need to handle Left and Right since they are used for other purposes

    # @staticmethod
    # def send_serial_message(message, com_port='/dev/ttyUSB0', baud_rate=9600):
    #     try:
    #         with serial.Serial(com_port, baud_rate) as ser:
    #             ser.write(message.encode())
    #     except serial.SerialException as e:
    #         print(f"{e}")
        
