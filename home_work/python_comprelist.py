#Append adds any element to the list,you can add a single
#element or multipel element
#Extend it concatinate to the list,but you can only add a list of value
numList = [2000, 2003, 2005, 2006]
stringList = ["Essential", "Python", "Code"]
mixedList = [1, 2, "three", 4]
#subList = [1,2,3, ["Copyright", 2006]]
listList = [numList, stringList, mixedList]#[[2000,2003,2005,2006],["Essential", "Python", "Code"],[1, 2, "three", 4]]
print (listList)
print (listList[1][0])

appendList = []
extendList = []

for ei in listList:
    #print ei
    appendList.append(ei)
    #print (appendList)
    extendList.extend(ei)
    #print (extendList)
print ("Appended List",appendList)
print ("Extended List",extendList)
