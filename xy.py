import pyautogui as pg
import time as t
t.sleep(5)
for i in range(4):
    pg.write("Hi bro")
    t.sleep(0.5)
    pg.press("Enter")