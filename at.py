import pyautogui as pg
import time
time.sleep(5)
for i in range(5):
    pg.write("Hi Uday bro")
    time.sleep(0.5)
    pg.press("Enter")