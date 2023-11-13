import tkinter as tk
import random
from SmartLight import LightController

class CameraController():
    def __init__(self, window, big_txt, light_controller):
        self.window = window
        self.big_txt = big_txt
        self.status = "Off"
        self.motion = "No"
        self.light_controller = light_controller

        self.setup_gui()
    
    def setup_gui(self):
        self.title_lb = tk.Label(text="Front Door Camera Motion Detection")
        self.title_lb.pack()

        self.detect_button = tk.Button(text="Random Detect Motion", command=self.detect_motion)
        self.detect_button.pack()

        self.button = tk.Button(text="Toggle On\Off", command=self.setup_status)
        self.button.pack()

        self.motion_lb = tk.Label(text=f"Front Door Camera - Motion {self.motion}")
        self.motion_lb.pack()

        self.auto_rule = tk.Label(text="Automation Rule: Turn on lights when motion is detected")
        self.auto_rule.pack()
        
    def detect_motion(self):
        if self.status == "On":
            if random.randint(1, 3) in [1, 2]:
                self.motion = "Yes"
                self.motion_lb["text"] = f"Front Door Camera - Motion {self.motion}"
                self.light_controller.set_status("On")
            else:
                self.motion = "No"
                self.motion_lb["text"] = f"Front Door Camera - Motion {self.motion}"
        else:
            self.motion = "No"

    def setup_status(self):
        if self.status == "Off":
            self.status = "On"
        else:
            self.status = "Off"
        self.big_txt.delete("3.0", "3.end")
        self.big_txt.insert("3.0", f"Front Door Camera: SecurityCamera Status: {self.status}")