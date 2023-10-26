import tkinter as tk
from tkinter import PhotoImage, filedialog
import customtkinter

from presentation.UseCase import UseCase
from presentation.view.CommandButton import CommandButton
from presentation.view.DisplayScreen import DisplayScreen
from presentation.view.MovementButton import MovementButton
from presentation.view.SettingButton import SettingButton
from presentation.view.SwitchButton import SwitchButton

# Uncomment the next line when running on a Raspberry Pi
# import RPi.GPIO as GPIO

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):

    def __init__(self, root):

        # Initialize GPIO for the Setting button
        GPIO.setmode(GPIO.BCM)  
        self.setting_pin = 17  # Assuming pin 17 for the Setting button
        GPIO.setup(self.setting_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


        # Setting the main window properties
        self.root = root
        self.root.title("PiApp")
        self.root.geometry("1024x600")
        self.root.configure(bg="white")
        self.use_case = UseCase(self)

        # Creating widgets   
        # self.settings_button = SettingButton(self.root, command=self.handle_setting_button)     
        self.settings_button = SettingButton(self.root, command=lambda: UseCase.button_callback("Setting"))
        self.settings_button.pack(anchor="ne")

        # Camera or Image display
        self.display_screen = DisplayScreen(self.root)
        self.display_screen.pack(expand = True, fill= "both")

        # Switch between live camera and image gallery
        self.live_camera = False

        #ofNoUse
        x = self.display_screen.winfo_width()
        y = self.display_screen.winfo_height()
        print("Width:", x)
        print("Height:", y)

        self.switch_button = SwitchButton(self.root, text="Switch to Gallery", command=lambda:self.use_case.switch_display(x=x,y=y))
        self.switch_button.pack(anchor="center", padx=10, pady=10)

        #Controllers
        self.movement_button = MovementButton(self.root)
        self.movement_button.pack(side=tk.LEFT, anchor="sw", padx=10, pady=10)

        self.command_button = CommandButton(self.root)
        self.command_button.pack(side=tk.RIGHT,anchor="se",padx=10, pady=10)

        # Initialize GPIO (mock code, uncomment and modify for actual use on Raspberry Pi)
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Assuming pin 17 for camera input

        # def handle_setting_button(self):
        #     # Read the GPIO input
        #     button_state = GPIO.input(self.setting_pin)
            
        #     # Handle the GPIO input and display output
        #     if button_state == GPIO.LOW:
        #         print("Setting button pressed!")
        #         # Any other actions or logic you want to perform
        #     else:
        #         print("Setting button not pressed!")


root = tk.Tk()
app = App(root)
root.mainloop()