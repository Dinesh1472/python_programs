#Purpose:Set Example 

temp = {10,20,'hi','welcome',20,'Hi'}
print ("temp set contains:",temp)
#print (list(temp))
#'''
temp1 = ['hi', 'Hi', 20, 10,10,'hi','welcome','bye']
temp1 = set(temp1)
print ("temp set1 contains:",temp1)
temp3 = temp.union(temp1)
print ("Union of Two set value is :",temp3)

temp4 = temp.intersection(temp1)
print ("Intersection of Temp4 is:",temp4)
