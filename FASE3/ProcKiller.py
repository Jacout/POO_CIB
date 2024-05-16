"""Importamos ctypes 

Creamos un handle para User32.dll y para Kernel32.dll 

Es una variable que nos da acceso de todos los modos a las funciones que vamos a realizar (estándar, sincronizado, error). 

Capturamos el nombre de la ventana que queremos cerrar e intentamos obtener un handle de esa ventana. 

Si el resultado de la función anterior es 0, resulta que ocurrió un error, por lo que informamos del error al usuario y cerramos el script. 

Si no se dieron errores implica que si obtuvimos el handle y buscaremos obtener el ID del proceso asociado a esa ventana. 

Si la respuesta de GetWindowThreadProcessId es 0, significa que ocurrió un error, por lo que informamos al usuario y terminamos el script. 

Si no hubo error, tenemos el ID del proceso (PID), por lo que definimos el tipo de acceso, limitamos la herencia de los subprocesos y copiamos a una nueva variable el PID. Con estos datos intentamos obtener el handle del proceso abierto en la variable hProcess. 

Si la variable hProcess tiene un valor menor o igual a cero, significa que hubo un error. Actuaremos en consecuencia para terminar el script. 

Si no hubo error, significa que tenemos el handle del proceso y definiremos el código de salida como 1 (podemos usar otro valor). Usaremos la función TerminateProcess para terminar el proceso sobre el cual tenemos privilegios que está en hProcess. 

Si la respuesta obtenida de TerminateProcess es 0, significa que hubo un error, por lo que actuaremos en consecuencia. 

Si no hubo error, significa que logramos terminar el proceso y la ventana se cerró. Informamos al usuario con un mensaje. """

import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll")
u_handle = ctypes.WinDLL("User32.dll")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

lpWindowName = ctypes.c_char_p(input("Enter Window Name to Kill: ").encode('utf-8'))
hWnd = u_handle.FindWindowA(None, lpWindowName)

if hWnd == 0:
    msgError = "Error Code: {0} - Could Not Grab Handle"
    print(msgError.format(k_handle.GetLastError()))
    exit(1)
else:
    print("Got the Handle!")
    lpdwProcessId = ctypes.c_ulong()
    response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessId))
    if response == 0:
        msgError = "Error Code: {0} - Could Not Grab PID"
        print(msgError.format(k_handle.GetLastError()))
        exit(1)
    else:
        print("Got the PID!")
        dwDesiredAccess = PROCESS_ALL_ACCESS
        bInheritHandle = False
        dwProcessId = lpdwProcessId
        hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
        if hProcess <= 0:
            msgError = "Error Code: {0} - Could Not Grab Priv Handle"
            print(msgError.format(k_handle.GetLastError()))
        else:
            print("Got our Handle...")
            uExitCode = 0x1
            response = k_handle.TerminateProcess(hProcess, uExitCode)
            if response == 0:
                msgError = "Error Code: {0} - Could Not Terminate Process"
                print(msgError.format(k_handle.GetLastError()))
            else:
                print("Process Went Bye Bye!")
