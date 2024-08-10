try:
    temp=15
    if temp>10:
        print("Above ten,")
        if temp>20:
            print("And also above 20!")
        else:
            print("But not above 20")
 
finally:
    print("nested if")
