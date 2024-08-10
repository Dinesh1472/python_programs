import os
try:
    directory ='Dinesh'
    parent_dir =r'c:\python_learning\Author'
    path =os.path.join(parent_dir,directory)
    os.makedirs(path)
    print("directory'%s'created"%directory)

except Exception as e:
    print(e)
