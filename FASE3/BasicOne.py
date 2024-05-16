'''
BasicOne.py
Script to display string 
passed to script from PowerShell
'''


"""Se importa el módulo sys, el cual se necesita para el proceso de pasar datos a través del pipeline. 
Se imprime un mensaje desde Python para demostrar que este script si se está ejecutando. 
Procesa cada línea enviada al script vía el pipeline e imprime su contenido (línea por línea). En el ejemplo solo estamos pasando una línea. 
"""

# import standard module sys
import sys

print("Welcome to Python\n")
print("Data Received from PowerShell\n")

for eachLine in sys.stdin:
    print("Hi",eachLine)


