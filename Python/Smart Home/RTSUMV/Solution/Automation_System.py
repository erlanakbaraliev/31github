import tkinter as tk
from SmartLight import LightController
from Thermostat import ThermostatController
from Camera import CameraController

class AutomationSystem:
    def __init__(self, window):
        self.window = window
        self.window.title("Smart Home")

        self.setup_gui()

    def setup_gui(self):
        self.window.rowconfigure(0, minsize=50, weight=1)
        self.window.columnconfigure(0, minsize=50, weight=1)

        self.setup_text()

        light_controller = LightController(self.window, self.big_txt)
        thermostat_controller = ThermostatController(self.window, self.big_txt)
        camera_controller = CameraController(self.window, self.big_txt, light_controller)

    def setup_text(self):
        self.big_txt = tk.Text(relief=tk.SUNKEN)
        self.big_txt.pack()

        self.big_txt.insert("1.0", "Living Room Light: SmartLight Status: Off\n")
        self.big_txt.insert("2.0", "Living Room Thermostat: Thermostat Status: Off\n")
        self.big_txt.insert("3.0", "Front Door Camera: SecurityCamera Status: Off\n")

window = tk.Tk()
app = AutomationSystem(window)
window.mainloop()