import os
try:
    path =r"D:\"
    os.rmdir(path)
except Exception as e:
    print(e)
