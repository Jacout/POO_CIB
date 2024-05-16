"""Cuando recolectamos información para un proyecto, el conocer la tecnología utilizada para la construcción de un sitio web nos permitirá hacer un mejor análisis de posibles vulnerabilidades para así brindar recomendaciones de seguridad. Si queremos verificar las tecnologías de un sitio web podemos usar el módulo builtWith. 
        Dicho módulo posee un método llamado parse que recibe la URL del sitio como parámetro y nos despliega las tecnologías usadas por el sitio. 
"""
    
import builwith

dominio = input("Ingresar algun domnio")
info = builwith.parse(dominio)
for key,value in info.items():
    print(key,"->",value)