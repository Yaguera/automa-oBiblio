import pyautogui
import time
import pyperclip


pyautogui.PAUSE = 0.5

time.sleep(5)
#titulo
pyautogui.hotkey('ctrl',"c")
titulo = pyperclip.paste()
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
subtitulo = pyperclip.paste()
pyautogui.hotkey('alt','tab')
pyautogui.press('enter')
pyautogui.rightClick(x=458, y=361)
pyautogui.press('down', presses=6)
pyautogui.press('enter')
pyautogui.press('backspace',presses=2)
pyperclip.copy(titulo)
pyautogui.hotkey('ctrl','v')
pyautogui.press('tab')
if subtitulo != '-':
        pyperclip.copy(subtitulo)
        pyautogui.hotkey('ctrl',"v")
pyautogui.press('enter')
pyautogui.click(x=631, y=465)
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#autor
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
first_name = pyperclip.paste()
pyautogui.hotkey('alt','tab')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','r')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','r')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyperclip.copy(first_name)
pyautogui.hotkey('ctrl','v')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
last_name = pyperclip.paste()
pyautogui.hotkey('alt','tab')
if first_name != last_name:
        pyautogui.press('space')
        pyperclip.copy(last_name)
        pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('f12')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#classNum
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
pyautogui.hotkey('alt','tab')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

#classAutor
pyautogui.press('enter')
pyautogui.doubleClick(x=516, y=396)
pyautogui.rightClick(x=517, y=369)
pyautogui.press('down', presses=6)
pyautogui.press('enter')
pyautogui.hotkey('ctrl','c')
pyautogui.press('enter')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)
pyautogui.press('right')
pyautogui.hotkey('ctrl','v')

#SALINHA#
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
local = pyperclip.paste()        
pyautogui.hotkey('alt','tab')
#caso seja Sala de Leitura, trocar a classAutor
if local == 'Sala de Leitura':
        pyautogui.press('up')
        pyautogui.press('enter')
        pyautogui.press('tab', presses=3)
        pyautogui.press('delete', presses=30)
        pyautogui.write(last_name[:3].upper())
        pyautogui.press('enter')
        with pyautogui.hold('alt'):
                pyautogui.press(['tab','tab'])
        time.sleep(1)
        pyautogui.press('left')
        pyautogui.write(last_name[:3].upper())
        pyautogui.press('right')
        pyautogui.hotkey('alt','tab')
pyautogui.press('enter')

if local == '-':
        pyautogui.click(x=363, y=407)
        pyautogui.press('enter')
else: 
        pyautogui.press('backspace', presses=50)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('f12')
        pyautogui.press('enter')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#descritor
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
pyautogui.hotkey('alt','tab')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','r')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','r')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','r')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('f12')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#edição
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
edicao = pyperclip.paste()
pyautogui.hotkey('alt','tab')
pyautogui.press('down',presses=2)
pyautogui.press('enter')
pyautogui.hotkey('ctrl',"c")

pyautogui.press('backspace')
edicao_atual = pyperclip.paste()

pyautogui.write(edicao)
pyautogui.press('enter')

with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#dataPubli
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
pyautogui.hotkey('alt','tab')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#editora
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
pyautogui.hotkey('alt','tab')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','r')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('f12')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#cidade
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
pyautogui.hotkey('alt','tab')
pyautogui.press('down',presses=2)
pyautogui.press('enter')
pyautogui.hotkey('ctrl','r')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('f12')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#estado
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
pyautogui.hotkey('alt','tab')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','r')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('f12')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#ISBN
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
pyautogui.hotkey('alt','tab')
pyautogui.press('down',presses=3)
pyautogui.press('enter')
pyautogui.rightClick(x=459, y=380)
pyautogui.press('down', presses=6)
pyautogui.press('enter')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#tipo
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
pyautogui.hotkey('alt','tab')
pyautogui.press('down',presses=1)
pyautogui.press('enter')
pyautogui.hotkey('ctrl','r')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('f12')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#Serie
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
serie = pyperclip.paste()
pyautogui.hotkey('alt','tab')
pyautogui.press('enter')
pyautogui.rightClick(x=409, y=363)
pyautogui.press('down', presses=6)
pyautogui.press('enter')
pyautogui.hotkey('ctrl','c')
atual = pyperclip.paste()
pyautogui.press('backspace')
if serie == '-':
        pyautogui.press('f12')
        pyautogui.press('down', presses=3)
elif serie == '-' and atual != '':
        pyautogui.press('enter', presses=2)
        pyautogui.press('down', presses=2)
else: 
        pyperclip.copy(serie)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        pyautogui.click(x=633, y=464)
        pyautogui.press('down', presses=2)
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#qtdpaginas
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
pyautogui.hotkey('alt','tab')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
with pyautogui.hold('alt'):
        pyautogui.press(['tab','tab'])
time.sleep(1)

#ilustrado e ilustrador
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
ilustrado = pyperclip.paste()
pyautogui.press('right')
pyautogui.hotkey('ctrl',"c")
ilustrador = pyperclip.paste()
pyautogui.hotkey('alt','tab')   

if ilustrado == 'Sim':
        pyautogui.press('down', presses=3)
        pyautogui.press('enter')
        pyautogui.press('up')
        pyautogui.press('enter')
        #adicionar ilustrador
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl','r')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.press('f12')
        pyautogui.press('f12')
else:
        pyautogui.press('f12')
time.sleep(5)

#ativar
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('down',presses=5)
pyautogui.press('enter')
pyautogui.press('up',presses=4)
pyautogui.press('enter')
pyautogui.press('down',presses=6)
pyautogui.press('enter')
pyautogui.rightClick(x=409, y=363)
pyautogui.press('down', presses=6)
pyautogui.press('enter')
pyautogui.write('Codigo Reaproveitado')
pyautogui.press('enter')