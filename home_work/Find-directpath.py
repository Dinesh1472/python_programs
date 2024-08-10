import os
import traceback

filePath = input("Enter the directory path:")
#'''
fileList = os.listdir(filePath)
print (fileList)
outPutList = []
for eItem in fileList:
    if os.path.isdir(os.path.join(filePath,eItem)): 
        fullPath = os.path.join(filePath,eItem)
        print ("Directory name is:",fullPath)
        for eFile in os.listdir(fullPath):
            fullPath1 = os.path.join(fullPath,eFile)
            if fullPath1.endswith('.py'):
                outPutList.append(eFile)
print (outPutList)
print('number of python file list :',len(outPutlist))
