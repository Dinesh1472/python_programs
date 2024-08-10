import os
try:
     var=input("enter ip adress:")
     print(var)
     cmdstring=os.popen("ping "+var).read()
     print(cmdstring)
     if "Reply from" in cmdstring:
          print("ipadress:"+var+"is active")
                   
except exception as e:
     print()
