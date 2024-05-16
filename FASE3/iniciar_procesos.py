"""Importamos ctypes y los tipos de datos de ctypes 

Creamos un handle para el Kernel32.dll 

Creamos la clase STARTUPINFO que emula la estructura procedente de C++. 

Creamos la clase PROCESS_INFORMATION que emula la estructura procedente de C++. 

Definimos todas las variables que necesitamos. 

Invocamos el método CreateProcessW. 

Si la respuesta no es cero, significa que la función si realizó tu tarea con éxito. 
"""

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
