try:
    tempvar=int(input("enter the channel no:"))
    print(tempvar)
    if tempvar>0:
        if tempvar%5==0:
            print("channel number "+str(tempvar)+ "belong to zee")
        elif tempvar%7==0:
            print("channel number "+str(tempvar)+ "belong to vijay")
        else:
            print("channel number "+str(tempvar)+ "belong to sun tv")
finally:
    print()
