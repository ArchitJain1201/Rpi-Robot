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


    def load_images_from_directory(self, directory):
        self.image_paths = []  # Initialize the list once
        valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(valid_extensions):
                    full_path = os.path.join(root, file)
                    self.image_paths.append(full_path)

    def update_image_display(self):
        if not self.image_paths:
            print("No images found in the directory.")
            return

        if os.path.isfile(self.image_paths[self.current_image_index]):
            image = Image.open(self.image_paths[self.current_image_index])
            screen_height = self.app.display_screen.winfo_height()
            aspect_ratio = image.width / image.height
            new_width = int(screen_height * aspect_ratio)
            image = image.resize((new_width, screen_height), Image.Resampling.LANCZOS)
            self.image = ImageTk.PhotoImage(image)

            # Assuming you have a canvas or similar widget to display the image
            screen_width = self.app.display_screen.winfo_width()
            x_position = screen_width // 2
            self.app.display_screen.create_image(x_position, screen_height // 2, image=self.image, anchor="center")
        else:
            print(f"Not a file: {self.image_paths[self.current_image_index]}")


    # def update_image_display(self):

    #     # Get the actual dimensions of the display screen
    #     self.app.root.update()  # This ensures the window is updated
    #     screen_height = self.app.display_screen.winfo_height()

    #     self.current_image_index = 0  # Start with the first image

    #     if os.path.isfile(self.image_paths[self.current_image_index]):
    #         image = Image.open(self.image_paths[self.current_image_index])

    #         # Calculate the new width maintaining the aspect ratio
    #         aspect_ratio = image.width / image.height
    #         new_width = int(screen_height * aspect_ratio)

    #         # Resize the image to fit the y-axis of the screen
    #         image = image.resize((new_width, screen_height), Image.Resampling.LANCZOS)
    #         # image = image.resize((new_width, screen_height), Image.ANTIALIAS)
    #         self.image = ImageTk.PhotoImage(image)

    #         # Calculate position to center the image on the screen
    #         screen_width = self.app.display_screen.winfo_width()
    #         x_position = screen_width // 2

    #         # Create image in the center of the canvas
    #         self.app.display_screen.create_image(x_position, screen_height // 2, image=self.image, anchor="center")

    #     else:
    #         print(f"Not a file: {self.image_paths[self.current_image_index]}")

    # def switch_display(self, x=1000, y=1000):
    #     if self.app.live_camera:
    #         self.app.switch_button.set_text("Switch to Gallery")
    #         # Switch to image from gallery
    #         self.image_paths= filedialog.askopenfilename(title="Select an Image",filetypes=[("Image files", ("*.png", "*.jpg", "*.jpeg")), ("All files", "*.*")])
    #         self.current_image_index = 0
    #         if self.image_paths:
    #             self.update_image_display()

    #     else:
    #         self.app.switch_button.set_text("Switch to Live Camera")
    #         # Mock code for displaying camera input, replace with actual camera input code

    #     self.app.live_camera = not self.app.live_camera

    def switch_display(self, x=1000, y=1000):
        # This method is for toggling between live camera and image gallery mode
        self.app.live_camera = not self.app.live_camera
        if self.app.live_camera:
            self.app.switch_button.set_text("Switch to Gallery")
            # Code to display live camera feed
        else:
            self.app.switch_button.set_text("Switch to Live Camera")
            # Code to display the image gallery
            self.load_images_from_directory('C:/Users/Archit Jain/Desktop/Rpi-Robot/Gallery')
            self.update_image_display()  # Update to show the current image

    def next_image(self):
        if not self.app.live_camera and self.image_paths:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.update_image_display()

    def previous_image(self):
        if not self.app.live_camera and self.image_paths:
            
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.update_image_display()

    def button_callback_m(self,button_name):
        if self.app.live_camera:  # Assuming 'app' is accessible here, or pass it as an argument
            print(f"{button_name} button pressed")
        else:
            if button_name == "Up":
                print(f"{button_name} button pressed")
                self.previous_image()
            elif button_name == "Down":
                self.next_image()
        
