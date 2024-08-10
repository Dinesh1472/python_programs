import os

# folder path
dir_path = r'E:\\\\\'
count =0
# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    print(path)
    #if os.path.isfile(os.path.join(dir_path, path)):
     #   res.append(path)
    count +=1

        
#print(res)
print('File count :',count)
