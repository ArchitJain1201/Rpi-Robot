from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk

class UseCase:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def button_callback(button_name):
        print(f"{button_name} button pressed")

    def switch_display(self, x=1000, y=1000):
        if self.app.live_camera:
            self.app.switch_button.set_text("Switch to Gallery")
            # Switch to image from gallery
            file_path = filedialog.askopenfilename(title="Select an Image",filetypes=[("Image files", ("*.png", "*.jpg", "*.jpeg")), ("All files", "*.*")])
            if file_path:

                # Get the actual dimensions of the display screen
                self.app.root.update()  # This ensures the window is updated
                screen_height = self.app.display_screen.winfo_height()

                # Open the image
                image = Image.open(file_path)

                # Calculate the new width maintaining the aspect ratio
                aspect_ratio = image.width / image.height
                new_width = int(screen_height * aspect_ratio)

                # Resize the image to fit the y-axis of the screen
                image = image.resize((new_width, screen_height), Image.Resampling.LANCZOS)
                self.image = ImageTk.PhotoImage(image)

                # Calculate position to center the image on the screen
                screen_width = self.app.display_screen.winfo_width()
                x_position = screen_width // 2

                # Create image in the center of the canvas
                self.app.display_screen.create_image(x_position, screen_height // 2, image=self.image, anchor="center")

        else:
            self.app.switch_button.set_text("Switch to Live Camera")
            # Mock code for displaying camera input, replace with actual camera input code

        self.app.live_camera = not self.app.live_camera


    # @staticmethod
    # def send_serial_message(message, com_port='/dev/ttyUSB0', baud_rate=9600):
    #     try:
    #         with serial.Serial(com_port, baud_rate) as ser:
    #             ser.write(message.encode())
    #     except serial.SerialException as e:
    #         print(f"{e}")
        
