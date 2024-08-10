import socket
try:
    inputval=input("enter the ipaddress :")
    hostname=socket.gethostname()
    ipadd=socket.gethostbyname(hostname)
    print("your computer name is:"+hostname)
    print("your ip address is :"+ipadd)
    if inputval==ipadd:
        print("it matches with the entered value :")
    else:
        print("it does not match !")

except exception as e:
    print("IP addres")
