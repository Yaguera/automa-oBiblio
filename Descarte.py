import pyautogui
import time
import pyperclip

pyautogui.PAUSE=0.3
time.sleep(5)


for i in range(17):
    pyautogui.hotkey('ctrl','c')
    registro = pyperclip.paste()
    pyautogui.press('right')
    pyautogui.hotkey('ctrl','c')
    exemplar = pyperclip.paste()
    pyautogui.hotkey('alt','tab')
    pyautogui.click(x=524, y=359)
    pyautogui.write(registro)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=640, y=215)
    if exemplar != 1:
        pyautogui.press('down',presses = int(exemplar))
    else:
        pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('down',presses=5)
    pyautogui.press('enter')
    pyautogui.press('down',presses=4)
    pyautogui.press('enter')
    pyautogui.press('f12')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','f3')
    pyautogui.rightClick(x=524, y=359)
    pyautogui.press('down',presses=6)
    pyautogui.press('enter')
    pyautogui.press('delete')
    with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('left')
