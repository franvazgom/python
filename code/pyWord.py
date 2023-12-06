import pyautogui 
import pygetwindow as gw
import clipboard
import time
pyautogui.hotkey('win', 's')  # Abre el menú de inicio de Windows
pyautogui.write('passwordsReload')       # Escribe "Word" en la búsqueda
time.sleep(1)
pyautogui.press('enter')      # Presiona Enter para abrir Word
time.sleep(2)  # Espera 5 segundos (ajusta según sea necesario)
pyautogui.write('hansson')
pyautogui.press('enter')

active_window = gw.getActiveWindow()
titulo = active_window.getTitle()
print(titulo)
titulos = gw.getAllTitles()
print(titulos)

pyautogui.hotkey('ctrl', 'a')       # Selecciona todo el texto en la ventana activa
pyautogui.hotkey('ctrl', 'c')       # Copia el texto seleccionado al portapapeles

text = clipboard.paste()  # Obtiene el texto del portapapeles
print(text)
