
try:
        def myFun(**kwargs):
         print(kwargs)
        for key, value in kwargs.items():
            print('%s==%s'%(key,value))

        myFun(first='geeks',mid='for',last='geeks')

except Exception as e:
    print(e)
