#add element into dict
try:
    dict ={}
    print('empty dict :')
    print(dict)

    dict[0]='elegant'
    dict[2]='for'
    dict[3]=1
    print(dict)

    dict['value']=2,3,4
    print(dict)

    dict[5]={'nested':{'1':'life',2:'geeks'}}
    print(dict)


except Exception as e:
    print(e)


