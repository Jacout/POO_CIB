import subprocess


"""El resultado del comando será almacenado en una variable, en este caso, runningProcesses. Esta es una variable de tipo bytes, por lo que requiere ser decodificada para convertirse en un str. 

La librería subprocess tiene el método check_output el cual toma el parámetro que recibe como la línea de comando que tu quieres ejecutar. Si ejecutamos el contenido de ese parámetro como un comando directamente en PowerShell (o en CMD) nos devolverá el mismo resultado que lo que obtuvimos de resultado en Python. La explicación de como se compone la línea enviada como parámetro es: 

powershell - Es el proceso (intérprete) a ejecutar 

-Executionpolicy ByPass - PowerShell no ejecutará scripts o CmdLets sin permiso explícito, este parámetro especifíca que puede ejecutar el comando sin bloquear nada y sin lanzar advertencias o desplegados en una terminal aparte. 

-Command - Nos permite especificar que lo que sigue es un comando de PowerShell. Si necesitamos ejecutar un script deberemos cambiarlo por -File y escribir un nombre válido de script de PowerShell. 

Get-Process - Es el nombre del CmdLet que se ejecutará, en este caso, sin parámetros. """

comando = "Get-Process"
lineaPS = "powershell -Executionpolicy ByPass -Command "+ comando
runningProcesses = subprocess.check_output(lineaPS)
print(runningProcesses.decode())

