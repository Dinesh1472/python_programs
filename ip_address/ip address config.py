import platform
import os
try:
    osidentifier=platform.platform()
    print(osidentifier)
    if "Window" in osidentifier:
        print("underlying os is window")
        cmdstring="ipconfig"
        
    elif "drawn" in osidentifier or "sonam"in osidentifier:
        print("underlying os is mac")
        cmdstring="ifconfig"
        
    else:
        print("underlying os is linux")
        cmdstring="ifconfig"

    var=os.popen(cmdstring).read()
    print(var)

except exception as e:
    print()
