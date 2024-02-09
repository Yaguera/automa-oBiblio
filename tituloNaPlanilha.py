import pyautogui
import time
import pyperclip

pyautogui.PAUSE=0.2
time.sleep(5)

for i in range(4):
    pyautogui.hotkey('ctrl','c')
    registro = pyperclip.paste()
    pyautogui.hotkey('alt','tab')
    pyautogui.click(x=524, y=359)
    pyautogui.write(registro)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=640, y=215)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=820,y=244)
    pyautogui.press('enter')
    pyautogui.rightClick(x=606,y=380)
    pyautogui.press('down',presses=6)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl','c')
    Titulo = pyperclip.paste()
    pyautogui.press('f12')
    pyautogui.press('f12')
    pyautogui.hotkey('ctrl','f3')
    pyautogui.rightClick(x=524, y=359)
    pyautogui.press('down',presses=6)
    pyautogui.press('enter')
    pyautogui.press('delete')
    with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
    time.sleep(1)
    pyautogui.press('left')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('down')
    pyautogui.press('right')