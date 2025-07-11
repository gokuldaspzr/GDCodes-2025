import tkinter as tk
from PIL import ImageGrab
import os

# Set your save location here
SAVE_LOCATION = "C:/Users/YourUsername/Pictures/screenshot.png"  # Change path as needed

def capture_screen():
    screenshot = ImageGrab.grab()
    # Ensure directory exists
    os.makedirs(os.path.dirname(SAVE_LOCATION), exist_ok=True)
    screenshot.save(SAVE_LOCATION)
    print(f"Screenshot saved at {SAVE_LOCATION}")

root = tk.Tk()
root.title("Screen Capture")

capture_btn = tk.Button(root, text="Capture Screen", command=capture_screen)
capture_btn.pack(pady=20, padx=20)

root.mainloop()