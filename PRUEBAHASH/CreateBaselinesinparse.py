''' 
Step One Create a baseline hash list of target folder
December 2018, Python Forensics

'''

''' LIBRARY IMPORT SECTION '''

import subprocess       # subprocess library
import os               # Operating System Path
import pickle           # Python object serialization 

'''ARGUMENT PARSING SECTION '''

def ValidatePath(thePath):
    ''' Validate the Folder thePath
        it must exist and we must have rights
        to read from the folder.
        raise the appropriate error if either
        is not true
    '''
    # Validate the path exists
    if not os.path.exists(thePath):
        print('Path does not exist')

    # Validate the path is readable
    if os.access(thePath, os.R_OK):
        return thePath
    else:
        print('Path is not readable')

#End ValidatePath ===================================

baselineFile = 'reportes/salida1.pickle'
targetPath   = 'C:\\Users\\Jacob\\Documents\\PROYECTOS\\PYTHON\\Proyect_P_CIB'
tmpFile      = os.path.abspath('reportes/salida1.txt')

print("baseline: ", baselineFile)
print("Target: ", targetPath)
print("tmpFile: ", tmpFile)

''' MAIN SCRIPT SECTION '''
if __name__ == '__main__':

    try:
        ''' POWERSHELL EXECUTION SECTION '''
        print()
        command = "powershell -ExecutionPolicy ByPass -File HashAcquire.ps1 -TargetFolder "+\
                  targetPath + " -ResultFile " + tmpFile 
        print(command)
        powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
        if powerShellResult.stderr == None:
            input("ya")
        
            ''' DICTIONARY CREATION SECTION '''
            baseDict = {}
            
            with open(tmpFile, 'r') as inFile:
                for eachLine in inFile:
                    lineList = eachLine.split()
                    if len(lineList) == 2:
                        hashValue = lineList[0]
                        fileName  = lineList[1]
                        baseDict[hashValue] = fileName
                    else:
                        continue
        
            with open(baselineFile, 'wb') as outFile:
                pickle.dump(baseDict, outFile)
                print("Baseline: ", baselineFile, " Created with:",
                      "{:,}".format(len(baseDict)), "Records")
                print("Script Terminated Successfully")
        else:
            print("PowerShell Error:", p.stderr)
            
    except Exception as err:
        print ("Cannot Create Output File: "+str(err))
        quit()
    
    
    
    
