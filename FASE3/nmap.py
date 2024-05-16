"""
Nmap es un potente escáner de puertos que
permite identificar puertos abiertos, cerrados o
filtrados, así como programar rutinas para encontrar
posibles vulnerabilidades en un host determinado. 
"""

import nmap

#tomas el rango de puertos
begin = 78
end = 80

#asiganas el ip a escanear

target = input("IP a escanear puertos")


#inicias la instancia del portscaner como objeto

scanner = nmap.PortScanner()

for i in range(begin,end+1):
    
    #escaneas el puerto 
    res = scanner.scan(target,str(i))
    
    #el resultado es un diccionario contiene
    #informacion que dice si esta abierto o cerrado
    #y el estado del puerto
    
    res = res['scan'][target]['tcp'][i]['state']
    print(f'port {i} is {res}.')