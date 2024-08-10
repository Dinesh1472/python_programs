import MySQLdb
import os
import traceback
#import PyMySQL # python 3
#import sys
#sys.path.append(r'C:\Python27\python Practise\Batch_19\DB_Connection')
import mysqlConfig


class getDailyData:

   def __init__(self):
      self.serverName = mysqlConfig.serverName
      self.userName = mysqlConfig.uid
      self.pwd = mysqlConfig.pwd
      self.dbName  = mysqlConfig.dbName
      self.fileName = 'testfile_1030AMbatch.csv'

   def getData(self):
      try:
         fobj = open(self.fileName,'w')
         fobj.write("ID"+','+"Name"+','+'course'+','+'PhoneNum'+'\n')
         # Open database connection
         db = MySQLdb.connect(self.serverName,self.userName,self.pwd,
                              self.dbName)
         cursor = db.cursor()        
         selectQuery = "SELECT * from pyrock"
         rowCount = cursor.execute(selectQuery)
         print rowCount
         rows = cursor.fetchall() #fetches all the rows from ur table.        
         print rows
         print rows
         for eachrow in rows:
            print eachrow
            fobj.write(str(eachrow[0])+','+eachrow[1]+','+str(eachrow[2])+','+str(eachrow[3])+'\n')         
      
      except Exception as e:
         print e
         
      finally:
         db.close()
         fobj.close()

#Defining object for the class
obj = getDailyData()

obj.getData()