# break statement
try:
    var=1
    while var<6:
        print(var)
        if var==3:
            break
        var +=1
    print("----------------------")

    #while statement
    num=1
    while num<200:
        print(num)
        num=num*2
    print("------------------")
    var=1
    while var<6:
         var +=1
    if var==3:
       continue
    print(var)

    print("---------------------------")


    var=1
    while var<6:
        print(var)
        var +=1
    else:
        print("var is no longer less than 6")

except exception as e:
    print()
