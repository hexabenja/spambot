import pyautogui
import time

f = open('spam', 'r')
time.sleep(5)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
