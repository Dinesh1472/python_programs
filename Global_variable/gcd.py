try:
    import math
    num1=int(input("enter the num1 :"))
    num2=int(input("enter the num2 :"))
    gcd_result=math.gcd(num1,num2)
    print("the GCD of",num1,"and",num2,"is",gcd_result)

except exception as e:
    print()
