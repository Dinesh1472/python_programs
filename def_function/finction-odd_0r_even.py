#a simple python function if  check
#whether x is even or odd
try:
    def evenodd(x):
        if (x % 2==0):
            print('even')

        else:
            print('odd')

    #call the function
    evenodd(2)
    evenodd(31)
    evenodd(32)

except Exception as e:
    print(e)
