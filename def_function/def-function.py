try:
    def demofun(value):
     var = 'My name is :'+value
     return var

    var=demofun('Dinesh')
    print(var)
except Exception as e:
    print(e)
