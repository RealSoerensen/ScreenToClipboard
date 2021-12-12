import pytesseract
from PIL import ImageGrab
import win32api
import pyautogui
import pyperclip

pytesseract.pytesseract.tesseract_cmd = f'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Not clicked
state_left = win32api.GetKeyState(0x01)
print("Ready!")
while True:
    # Get current state of left mouse button
    left_click = win32api.GetKeyState(0x01)
    # If left button is clicked
    if left_click != state_left:  
        # Get pos1 of mouse
        x1, y1 = pyautogui.position()
        # Change state to clicked
        state_left = left_click
        # Loop while left button is held down
        while left_click == state_left:
            left_click = win32api.GetKeyState(0x01)
        # When left button is released
        x2, y2 = pyautogui.position()
        # Set state_left to not clicked
        state_left = left_click

        # Check if starting pos was top left and ending pos is bottom right
        if x1 < x2 and y1 < y2:
            # Get image of area between pos1 and pos2
            try:
                img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            except SystemError as e:
                print(f"Error:", e)
            finally:    
                # Get text from image
                try:
                    text = pytesseract.image_to_string(img)
                    pyperclip.copy(text)
                    print("Copied to clipboard")
                except Exception as e:
                    print('Error:', e)