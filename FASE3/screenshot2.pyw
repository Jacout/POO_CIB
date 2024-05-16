import pyautogui
import datetime

im = pyautogui.screenshot()
fecha = datetime.datetime.now()
nombre = r'SS_'
nombre += str(fecha.strftime('%Y%m%d_%H%M%S'))
nombre +='.png'
im.save(nombre)
