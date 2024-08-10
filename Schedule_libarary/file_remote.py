#Description Delete older zip from a location
#----

import os.path,time
import sys
import datetime
from datetime import date,datetime,timedelta,time
import time

import logging
import schedule

try:
    logger=logging.getLogger('Sample Request')
    logger.setLevel(logging.DEBUG)

    fh =logging.FileHandler('deletecron.log')
    fh.setLevel(logging.DEBUG)

    fmtr =logging.Formatter("%(asctime)s[%(levelname)s]%(message)s",datefmt="%m/%d%r%|:%m:%s%p")
    fh.setFormatter(fmtr)
    logger.addHandler(fh)

    deleteDirectory =r"C:\test"
    decidedDeletedate=(date.today()-timedelta(7)).strftime("%y-%m-%d")
    print(decidedDeletedate)


    #Function Definition

    def deleteolderfiles():
        dirlist=os.listdir(deleteDirectory)
        for eachfile in dirlist:
            #zipfileloc=deleteDirectory+'\\'+eachzip
         fileloc =os.path.join(deleteDirectory,eachfile)#create a parent and child directory
         filecreateDate=os.path.getmtime(fileloc)#get the modified time of each file

         print(filecreateDate)
         filecreateDate =datetime.fromtimestamp(filecreateDate).strftime('%y-%m-%d')

         print(filecreateDate)
         if filecreateDate<decidedDeleteDate:
            #print zipfile loc
            #print zipfile create date


            #if os=='windows':

            delcommand ='del/F/S/Q\"{0}\"'.format(zipfileloc)
            print(delcommand)

            #if os=='linux':
            #delcommand ='del/F/S/Q\"{0}\'".Format(zipfileloc)
            #print delcommand\


            retrnval =os.system(delcommand)
            if not retrnval:
                logger.info("zip filename:"+eachfile+"with created date:"+filecreateDate+"has been deleted")

            if-name__=="__main__":

            #deleteolderfiles()
             schedule.every(5).minutes.do(deleteolderfiles)

            #Loops so that the scheduling tak
            #Keeps on running all time

            while True:
                #cheks whether a scheduled task is pending to run or not
                schedule.run_pending().time.sleep(2)

                

except Exception as e:
    print(e)
