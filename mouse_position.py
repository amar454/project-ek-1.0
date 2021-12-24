"""
This file is basically only for development purposes only, for finding mouse position.
"""
import pyautogui
import time
import pyperclip
from tkinter import Tk  
if __name__ == "__main__":
    time.sleep(5)
    to_cp = str(pyautogui.position()).replace("Point(", "")
    
    pyperclip.copy(to_cp.replace(")", ""))
    
    
    