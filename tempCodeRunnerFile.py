self.display_screen = DisplayScreen(self.root)
        self.display_screen.pack(expand = True, fill= "both")

        # Switch between live camera and image gallery
        self.live_camera = False
        x = self.display_screen.winfo_width()
        y = self.display_screen.winfo_height()
        print("Width:", x)
        print("Height:", y)
        self.switch_button = SwitchButton(self.root, text="Switch to Gallery", command=lambda:self.use_case.switch_display(x=x,y=y))
        self.switch_button.pack(anchor="center", padx=10, pady=10)