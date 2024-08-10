try:
    inputval=int(input("Enter the start range number :"))
    inputval2=int(input("Enter the stop range number :"))

    for var in range(inputval,inputval2):
        if var%2==1:
            print("Number :" +str(var) +"is prime")
    else:
            print("Number :" +str(var) +"is even")
except exception as e:
    print(e)
