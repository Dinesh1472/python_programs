import traceback

while True:
    try:
        n = input("please enter a integer:")
        n =int(n)
    except Exception as e:
        print(traceback.format_exc())
        print("Through exception '%s'",e)

        print("Invalid integer please try again")
    else:
        print("Great, you successfully entered an integer!")
        
