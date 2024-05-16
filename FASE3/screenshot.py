import pyautogui

im = pyautogui.screenshot()
print(im)
im.save(r'ss.png')
