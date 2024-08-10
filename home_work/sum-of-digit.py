inputlist =[10,20,30,'hi',40]
print(inputlist)

digitsum =0
for ei in inputlist:
    if type(ei)==int:
        digitsum +=ei
print('sum of all digit in the list :',digitsum)
          
