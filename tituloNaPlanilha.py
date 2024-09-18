import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.2
time.sleep(5)

# Função para calcular coordenadas relativas
def get_relative_coords(x_rel, y_rel, screen_width, screen_height):
    screen_resolution = pyautogui.size()
    screen_width_current, screen_height_current = screen_resolution.width, screen_resolution.height
    x_abs = int(x_rel * screen_width_current / screen_width)
    y_abs = int(y_rel * screen_height_current / screen_height)
    return x_abs, y_abs

# Dimensões do monitor original (substitua com as dimensões do monitor em que as coordenadas foram obtidas)
original_screen_width = 1280
original_screen_height = 800

# Coordenadas relativas (substitua pelos valores relativos às dimensões do monitor original)
rel_coords = {
    'coord_1': (820, 244),
    'coord_2': (524, 359),
    'coord_3': (640, 215),
    'coord_4': (606, 380)
}

for i in range(30):
    pyautogui.hotkey('ctrl', 'c')
    registro = pyperclip.paste()
    pyautogui.hotkey('alt', 'tab')
    
    # Calcular e usar coordenadas dinâmicas
    x, y = get_relative_coords(*rel_coords['coord_2'], original_screen_width, original_screen_height)
    pyautogui.click(x=x, y=y)
    pyautogui.write(registro)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    x, y = get_relative_coords(*rel_coords['coord_3'], original_screen_width, original_screen_height)
    pyautogui.click(x=x, y=y)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    x, y = get_relative_coords(*rel_coords['coord_1'], original_screen_width, original_screen_height)
    pyautogui.click(x=x, y=y)
    pyautogui.press('enter')
    pyautogui.rightClick(x=606, y=380)  # Right click is relative to another set of coordinates
    pyautogui.press('down', presses=6)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'c')
    Titulo = pyperclip.paste()
    pyautogui.press('f12')
    pyautogui.press('f12')
    pyautogui.hotkey('ctrl', 'f3')
    
    x, y = get_relative_coords(*rel_coords['coord_2'], original_screen_width, original_screen_height)
    pyautogui.rightClick(x=x, y=y)
    pyautogui.press('down', presses=6)
    pyautogui.press('enter')
    pyautogui.press('delete')
    with pyautogui.hold('alt'):
        pyautogui.press(['tab', 'tab'])
    time.sleep(0.5)
    pyautogui.press('left')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('down')
    pyautogui.press('right')
