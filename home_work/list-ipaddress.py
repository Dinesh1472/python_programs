iplist=['10.213.163.53','10.213.162.41','10.213.163.25','10.213.161.31','10.213.161.36']
for eitem in iplist:
    if eitem.split('.')[2]=='163':
      print(eitem)
print()
#hhfghf
iplist=['10.213.163.53','10.213.162.41','10.213.163.25','10.213.161.31','10.213.161.36']
templist=[]
for eitem in iplist:
    if eitem.split('.')[2]=='163':
      print(eitem)
      templist.append(eitem)
print('Result list is:',templist)
      
