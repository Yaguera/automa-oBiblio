import pyautogui
import time
import pyperclip

pyautogui.PAUSE=0.2
time.sleep(5)

for i in range(12):
    pyautogui.hotkey('ctrl','c')
    registro = pyperclip.paste()
    pyautogui.hotkey('alt','tab')
    pyautogui.click(x=399, y=345)
    pyautogui.write(registro)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=557, y=163)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.doubleClick(x=440, y=246)
    pyautogui.rightClick(x=379, y=361)
    pyautogui.press('down',presses=6)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','c')
    Titulo = pyperclip.paste()
    pyautogui.press('f12')
    pyautogui.press('f12')
    pyautogui.hotkey('ctrl','f3')
    pyautogui.click(x=399, y=345)
    pyautogui.press('home')
    pyautogui.press('delete',presses=10)
    with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
    time.sleep(1)
    pyautogui.press('left')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('down')
    pyautogui.press('right')