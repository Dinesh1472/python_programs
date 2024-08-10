try:
    list = [15,120,5,1,9,50]
    print(list)

    even,odd=0,0

    for eitem in list:
        if(eitem%2==0):
            even =even+1

        else:
            odd =odd+1
    print("Even number in the list :",even)
    print("odd number in the list :",odd)

except Exception as e:
    print(e)
