#import pyodbc
#import pymssql#for sql server
#import oraclecx#oracle
#import pymongo#mongo db
#import psycopg2#post gre sql
import MySQLdb
import os
import traceback
#import PyMySQL # python 3
#import sys
#sys.path.append(r'C:\Python27\python Practise\Batch_19\DB_Connection')
import mysqlConfig


def getData():
    try:
        fobj = open('testfile_1030AMbatch.csv','w')
        fobj.write("ID"+','+"Name"+','+'course'+','+'PhoneNum'+'\n')
        # Open database connection
        db = MySQLdb.connect(mysqlConfig.serverName,mysqlConfig.uid,
                             mysqlConfig.pwd,mysqlConfig.dbName)        
        # prepare a cursor object using cursor() method
        cursor = db.cursor()        
        selectQuery = "SELECT * from pyrock"
        # Select qSQL with id=4.
        rowCount = cursor.execute(selectQuery)
        print rowCount
        rows = cursor.fetchall() #fetches all the rows from ur table.        
        print rows
        for eachrow in rows:
            print eachrow
            fobj.write(str(eachrow[0])+','+eachrow[1]+','+str(eachrow[2])+','+str(eachrow[3])+'\n')
            #fobj.write(str(eachrow)+'\n')        
        
    except Exception,e:
        print e
      
    finally:
        fobj.close()
        db.close()
        
getData()
