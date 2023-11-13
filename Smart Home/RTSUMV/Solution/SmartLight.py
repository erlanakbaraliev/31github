import tkinter as tk
import random


class LightController:
    status = "Off"
    def __init__(self, window, big_txt):
        self.window = window
        self.big_txt = big_txt
        self.level = 0

        self.setup_gui()
        self.start_simulation()

    def setup_gui(self):
        self.title_lb = tk.Label(text="Living Room Light Brightness")
        self.title_lb.pack()

        self.scale_button = tk.Scale(from_=0, to=100, orient=tk.HORIZONTAL, command=self.setup_level)
        self.scale_button.pack()

        self.button = tk.Button(text="Toggle On\Off", command=self.setup_status)
        self.button.pack()

        self.level_lb = tk.Label(text=f"Living Room Light - {self.level}")
        self.level_lb.pack()

    def setup_level(self, given_level):
        if self.status == "On":
            self.level = int(given_level) + random.randint(-10, 10)            
            if self.level > 100:
                self.level = 100
            elif self.level < 0:
                self.level = 0

            self.level_lb["text"] = f"Living Room Light - {self.level}"

    def simulate_light(self):
        self.setup_level(self.scale_button.get())
        self.window.after(1000, self.simulate_light)

    def start_simulation(self):
        self.window.after(1000, self.simulate_light)

    def setup_status(self):
        if self.status == "Off":
            self.status = "On"
        else:
            self.status = "Off"

        self.big_txt.delete("1.0", "1.end")
        self.big_txt.insert("1.0", f"Living Room Light: SmartLight Status: {self.status}")

    def set_status(self, new_status):
        self.status = new_status
        self.big_txt.delete("1.0", "1.end")
        self.big_txt.insert("1.0", f"Living Room Light: SmartLight Status: {self.status}")
