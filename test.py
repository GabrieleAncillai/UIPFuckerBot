from pyautogui import vscroll
import time

if __name__ == '__main__':
    for x in range(10):
        time.sleep(1)
        vscroll(-200)
