# Steps:
# 1. Install python 
# 2. Run pip install pywin32 to have win32api, win32con ready
# 3. Run python MoveMouse.py to start the script
# 4. Run Ctrl-C to stop the script
# Bonus - to change the time interval, tune the number with timeInSeconds 

import win32api, win32con, time, random

def click():
    x = random.randint(50,100)
    y = random.randint(50,100)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

timeInSeconds = 5

while True:
    click()
    time.sleep(timeInSeconds)