import os

try:
    cwd =os.getcwd()
    print('current working directory:',cwd)

    #os.mkdir(r'c:\my_project')#it's helps tp create directory if that is not present

    os.chdir(r'c:\my_project')
    print(os.getcwd())

    os.chdir('..')
    print(os.getcwd())

except Exception as e:
    print(e)
