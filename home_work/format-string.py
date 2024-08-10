import socket
import os

try:
    hostname=socket.gethostname()
    print(hostname)
    ipaddress=socket.gethostbyname(hostname)
    print(ipaddress)
    pingcmd='{0}--{1}."{2}"'.format('ping','t',ipaddress)
    print(pingcmd)

except exception as e:
    print(e)
