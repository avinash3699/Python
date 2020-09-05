# Python program to take ScreenShot using PyAutoGUI module

# We have to install 'pyautogui' module before using it in our program

from pyautogui import screenshot
screen_shot = screenshot()
screen_shot.save("screenshot using python.jpeg")
print("ScreenShot taken..!")

