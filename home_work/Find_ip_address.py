import socket
try:
    hostname=socket.gethostname()
    ipadd=socket.gethostname(hostname)
    print("your computer name is:"+hostname)
    print("your ip address is :"+ipadd)
