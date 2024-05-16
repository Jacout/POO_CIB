# Import the required module to handle Windows API Calls
import ctypes

# Grab a handle to kernel32.dll
k_handle = ctypes.WinDLL("Kernel32.dll")

# Win API Call
# HANDLE OpenProcess(
# DWORD dwDesiredAccess,
# BOOL bInheritHandle,
# DWAORD dwProcessId
# );

# Access Rights
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

# Setting Up The Params
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = ctypes.c_ulong(int(input("Process ID: ")))


# Calling the Windows API Call
response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

# Check For Errors
error = k_handle.GetLastError()
if error != 0:
	print("Handle Not Created!")
	print("Error Code: {0}".format(error))
	exit(1)

# Check to see if we have a valid Handle
if response <= 0:
	print("Handle Not Created!")
elif response >= 1:
	print("Handle Created!")



"""Importamos ctypes 

Creamos un handle para el Kernel32.dll 

Definimos una variable para especificar el acceso completo (acorde a los permisos del usuario con los que usemos este script). 

Definimos los valores de los 3 parámetros de entrada de la función OpenProcess. 

Ejecutamos la función OpenProcess que almacenará en la variable response el resultado de intentar obtener el handle. 

Guardamos en la variable error el código del último error, en caso de que no sea 0, significa que hubo algún error. Informamos al usuario y terminamos el script. 

Si la respuesta obtenida en la variable response es igual o menor que 0, significa que la función no fue exitosa. Si la respuesta el mayor o igual a 1, si funcionó y ese valor es el identificador del proceso. """