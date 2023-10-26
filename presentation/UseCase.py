from tkinter import filedialog
import tkinter as tk
import RPi.GPIO as GPIO


class UseCase:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def button_callback(button_name):
        print(f"{button_name} button pressed")

    def switch_display(self, x=320, y=240):
        if self.app.live_camera:
            self.app.switch_button.set_text("Switch to Gallery")
            # Switch to image from gallery
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
            if file_path:
                self.image = tk.PhotoImage(file=file_path)
                self.app.display_screen.create_image(x, y, image=self.image)
        else:
            self.app.switch_button.set_text("Switch to Live Camera")
            # Mock code for displaying camera input, replace with actual camera input code

        self.app.live_camera = not self.app.live_camera
        
    def handle_setting_button(self):
        # Read the GPIO input
        button_state = GPIO.input(self.app.setting_pin)
        
        # Handle the GPIO input and display output
        if button_state == GPIO.LOW:
            print("Setting button pressed!")
            # Any other actions or logic you want to perform
        else:
            print("Setting button not pressed!")

    def __del__(self):
        GPIO.cleanup()

