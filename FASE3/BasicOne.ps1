"""Defines la variable local $Python, si solo tienes instalada una versión de Python y tienes correctamente direccionada tu variable PATH, solo será necesario escribir el nombre del intérprete de Python con su correspondiente extensión (exe). Si, por otra parte, tienes más de una versión de Python, deberás especificar la ruta completa al intérprete de Python que vayas a usar. 

Define la variable $Script, la cual contiene la ruta exacta del script de Python que vas a ejecutar. 

La variable local $Message se inicializa con el mensaje que vamos a enviar al script de Python. 

Esta línea pasa el contenido de la variable $Message al script de Python. El elemento principal aquí es el &, el cual tiene la función de direccionar PS para lanzar el programa externo. """



# Python Executable Definition
$Python = "python.exe"


# Python Scrip that I wish to execute
$Script = "C:\Users\marle\Downloads\PS y Python\BasicOne.py"


Write-Host "Pass a String to Python"
$Message = "Hello Python - Hello Universe"


$Message | & $Python $Script



