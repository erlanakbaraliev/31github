import tkinter as tk
import random

class ThermostatController:
    def __init__(self, window, big_txt):
        self.window = window
        self.big_txt = big_txt
        self.status = "Off"
        self.level = 0
        
        self.setup_gui()
        self.start_simulation()

    def setup_gui(self):
        self.title_lb = tk.Label(text="Living Room Thermostat Temperature")
        self.title_lb.pack()

        self.scale_button = tk.Scale(from_=0, to=40, orient=tk.HORIZONTAL, command=self.setup_level)
        self.scale_button.pack()

        self.button = tk.Button(text="Toggle On\Off", command=self.setup_status)
        self.button.pack()

        self.level_lb = tk.Label(text=f"Living Room Thermostat - {self.level}")
        self.level_lb.pack()

    def setup_level(self, given_value):
        if self.status == "On":
            self.level = int(given_value) + random.randint(-5, 5)
            if self.level > 40:
                self.level = 40
            elif self.level < 0:
                self.level = 0

            self.level_lb["text"] = f"Living Room Thermostat - {self.level}"
    
    def simulate_temp(self):
        self.setup_level(self.scale_button.get())
        self.window.after(1000, self.simulate_temp)

    def start_simulation(self):
        self.window.after(1000, self.simulate_temp)

    def setup_status(self):
        if self.status == "Off":
            self.status = "On"
        else:
            self.status = "Off"
        self.big_txt.delete("2.0", "2.end")
        self.big_txt.insert("2.0", f"Living Room Thermostat: Thermostat Status: {self.status}")