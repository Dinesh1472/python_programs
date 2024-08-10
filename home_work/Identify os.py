import platform
import os

try:
    osidentifier=platform.platform()
    print(osidentifier)
    if "Window" in osidentifier:
        print("underlying os is window")
    elif "drawn" in osidentifier or "sonam"in osidentifier:
        print("underlying os is mac")
    else:
        print("underlying os is linux")

except exception as e:
    print()
