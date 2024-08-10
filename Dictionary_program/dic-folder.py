import os
      
try:
     fileinfodict =dict
     folderinfo =r'c:\\python_learning'

     paths =[os.path.join[folderinfo.basename]]
     for basename in os.listdir(folderinfo):

       print(min(paths,key =os.path.getmtime))
     fileinfodict[folderinfo]= oslistdis(folderinfo)

     print(fileinfodict)

except Exception as e:
    print(e)
