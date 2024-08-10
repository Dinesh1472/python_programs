import traceback

def fileReadFun():#function definition
    try:
        fobj = open('urlfile.txt')
        fobj1 = open('result_url.txt','w')#if file does not exist it will create
        content = fobj.readlines()  
        print(content)
        for eline in content:
            print(eline)
           # if 'python 'in eline:
            name =eline.strip().split('.')[1]
            fobj1.write (name + '\n')

    except exception as e:
        print(traceback.format_exc())
    finally:
        fobj.close()
        fobj1.close()

fileReadFun()#function call
