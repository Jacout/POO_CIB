import subprocess
import time

i = 0
cant = 2
#while  True:
while i < cant:
    subprocess.Popen(['pythonw.exe', 'screenshot2.pyw'])
    i += 1
    time.sleep(3)
