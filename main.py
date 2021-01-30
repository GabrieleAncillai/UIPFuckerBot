import pyautogui
import time


def FindPathOnScreen(path):
    location = pyautogui.locateCenterOnScreen(f"images/{path}")
    print(f"{path}", location)
    if location:
        pyautogui.click(location)
        return True
    else:
        return False


if __name__ == '__main__':

    paths = [
        "continuar.png",
        "enviar_sus_respuestas.png",
        "puede_mejorar.png",
        "responda_las_preguntas.png"
    ]

    interval = 0.1  # In secs

    while True:
        time.sleep(interval)
        # For each path in paths
        for x in paths:
            value = FindPathOnScreen(x)
            # This breaks the loop when image found
            if value is not None:
                break