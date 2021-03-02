import pyautogui
import time
message = 10
while message > 0:
    time.sleep(3)
    pyautogui.typewrite('I love you\n')
    time.sleep(2)
    pyautogui.press('enter')
    message = message - 1
