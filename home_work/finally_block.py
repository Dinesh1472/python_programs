try:
    val=5/10
    print(val)
except zeroDivisionError:
    print("can't divide by zero")
finally:
    print("this is always executed")
