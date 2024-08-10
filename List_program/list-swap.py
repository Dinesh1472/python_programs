try:
    lists = ["oranges", "grapes", "bananas"]

    print(" before list:",lists)


    #swap elements at index 0 and 2
    lists[0], lists[2] = lists[2], lists[0]

    print(" After swap list:",lists)

except Exception as e:
    print(e)
