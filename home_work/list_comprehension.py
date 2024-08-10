import os
Filepath =input("Enter the directory path :")
outPlist = [ef for ef in os.listdir(Filepath) if ef.endswith('.py')]
print(outPlist)
