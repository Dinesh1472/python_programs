import traceback

def fileReadFun():#function definition
    try:
        fobj = open('file.txt','r')
        fobj1 = open('result_24_07.txt','w')#if file does not exist it will create
        content = fobj.readlines()  
        print(content)
        for eline in content:
            print(eline)
            if 'python 'in eline:
                name =eline.split(',')[0]
                fobj1.write (name + '\n')

    except exception as e:
        print(traceback.format_exc())


    finally:
        fobj.close()
        fobj1.close()

fileReadFun()#function call
