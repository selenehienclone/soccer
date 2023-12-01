import pyautogui
import time

# Get the screen width and height
screenWidth, screenHeight = pyautogui.size()

# Move the mouse to a starting position
pyautogui.moveTo(100, 100)

# Perform a click at the starting position
pyautogui.click()

# Pause for a moment (adjust as needed)
time.sleep(1)

# Perform a drag to a new position
pyautogui.dragTo(200, 200, duration=1)

# Optional: Release the mouse button
pyautogui.mouseUp()
