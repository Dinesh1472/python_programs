#add two number
try:
    a=float(input("enter A value :"))
    b=complex(input("enter B value :"))
    c=a+b
    print("sum :",c)
    print(type(a))
    print(type(b))
    print("---------------------------------------------")

    #sub two number
    a=int(input("enter  value A :"))
    b=int(input("enter value B :"))
    c=a-b
    print("sub :",c)
    print(type(c))
    print("---------------------------------------------")


    #multiply two number
    a=int(input("enter value A :"))
    b=int(input("enter value B :"))
    c=a*b
    print("mul :",c)
    print("----------------------------------------------")

    #division two number
    a=int(input("enter value A :"))
    b=int(input("enter value B :"))
    c=a/b
    print("division :",c)

    print("-------------------------------")
    # exponential
    base=2
    exp=5
    print("exponential value is:",base**exp)


    print("-----------------------------")
    #floor operators
    a=4
    b=3
    print(a//b)
except exception as e:
    print()



