#Write all the files name and file size from a folder and write into a txt or csv file
import os
import traceback
#filePath = r'C:\Personal\PythonScript\python-ppt\TechTra\FileProgram'
filePath =input("Enter the folder location :")
try:
    fobj = open('resultFile.csv','w')
    fobj.write('FileName'+','+'FileSize'+'\n')
    if os.path.exists(filePath):
        fileNameList = os.listdir(filePath)
        for eFile in fileNameList:
            print(eFile)
            fp = os.path.join(filePath,eFile)
            print (fp)
            fileSize = os.path.getsize(fp)
            print (fileSize)
            fobj.write(eFile+','+str(fileSize)+'\n')
        
    else:
        print ("File Location %s is not present"%filePath)

except:
    print (traceback.format_exc())

finally:
    fobj.close()
    
