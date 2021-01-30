from pyautogui import locateCenterOnScreen, click, vscroll
import time
from constants import PATHS


def FindPathOnScreen(path):
    location = locateCenterOnScreen(f"images/{path}")
    if location:
        click(location)
        time.sleep(.1)
        print(f"{path}", location)
        if path is PATHS.get("PM"):
            vscroll(-80)
        return True
    else:
        return False


if __name__ == '__main__':

    print("Program is Executing!")

    paths = ["AETO", "RLP", "PM", "ESR", "CONT"]

    interval = 0.05  # In secs

    while True:
        time.sleep(interval)
        # For each path in paths
        for x in paths:
            value = FindPathOnScreen(PATHS.get(x))
            # This breaks the loop when image found
            if value:
                break
