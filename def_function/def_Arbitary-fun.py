def urlFind(*val):
    return val
try:
    var =urlFind('www.facebook.com')
    print('val',var)
    var1 =urlFind('www.facebook.com','www.google.com')
    print('val',var1)
    var2 =urlFind('www.facebook.com','www.google.com','www.yahoo.com')
    print('val',var2)
except Exception as e:
    print(e)
