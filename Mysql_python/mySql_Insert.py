#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      smohapa2
#
# Created:     21-02-2015
# Copyright:   (c) smohapa2 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Mysql connector link
#https://dev.mysql.com/downloads/connector/python/
#Module Install link
#https://pypi.python.org/pypi/mysqlclient 
import MySQLdb
#import pyodbc
#import oracle_cx
#
import mysqlConfig
#import profile

def insertMySQLdb():

    try:
        # Open database connection
        db = MySQLdb.connect(mysqlConfig.serverName,mysqlConfig.uid,mysqlConfig.pwd,mysqlConfig.dbName)
        #db = MySQLdb.connect("localhost","root","mcafee12#","student" )    
        #db = MySQLdb.connect("localhost","root","mcafee12#","airtel" )    
        #db = MySQLdb.connect("localhost","root","mcafee12#","raslras" ) 
        # prepare a cursor object using cursor() method
        cursor = db.cursor()    
        # Select qSQL with id=4.
        #insertQuery = """ insert into studpython values(4,"nagaraj",'python')"""
        insertQuery = """insert into pyrock values(1,"Himansu",'8934453556','python','2018-09-29',32)"""
        print (insertQuery)
        cursor.execute(insertQuery)
        db.commit()   
        selectQuery = "select * from pyrock where name='Himansu'"
        cursor.execute(selectQuery)
        rows = cursor.fetchall()
        if rows:
            print "Data inserted sucessfully"
        else:
            print "Data is not inserted"
                
    except Exception,e:
        print e
        
    finally:
        if db:
            db.close()
            

def selectDataFromMySQLdb():

    try:
        fobj = open('RaslrasInfo.csv','w')
        #fobj.write("ID"+','+"SourceIp"+','+'SourcePort'+','+'destIp'+','+'destPort'+'\n')        
        fobj.write("ID"+','+"userid"+','+'password'+','+'Email'+','+'CreatedDate'+','+'Status'+'\n')        
        # Open database connection
        #db = MySQLdb.connect("localhost","root","mcafee12#","student" )    
        db = MySQLdb.connect("localhost","root","mcafee12#","raslras" )    
        # prepare a cursor object using cursor() method
        cursor = db.cursor()    
            # Select qSQL with id=4.
        #insertQuery = """ insert into studpython values(4,"nagaraj",'python')"""
        #insertQuery = """insert into pyrock values(24,"Sahadeba",'python','9742318513')"""
        selectQuery = """select * from userinfo"""
        print selectQuery
        rowNum = cursor.execute(selectQuery)
        rows = cursor.fetchall()
        print rows
        for eachRow in rows:
            print eachRow
            fobj.write(str(eachRow[0])+','+eachRow[1]+','+str(eachRow[2])+','+eachRow[3]+','+str(eachRow[4])+'\n')
        fobj.close()
        
        '''
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
        '''
        #db.commit()    
        # disconnect from server
        #db.close()
        
    except Exception,e:
        print e
        
    finally:
        if db:
            db.close()

insertMySQLdb()
#selectDataFromMySQLdb()