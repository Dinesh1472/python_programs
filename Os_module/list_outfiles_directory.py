#list out files &directory

import os
try:
    path ='/'
    dir_list =os.listdir(path)
    print("files and directory in'",path,"':")
    print(dir_list)

    os.remove()#it's used to remove or delete a file path
    #this method can't remove
    os.rmdir()
except Exception as e:
    print(e)
