#q1
try:
    print(int(6.1),int(6.78),int(6.99),float(7))
    print("-----------------------------")
    #q2
    i=1
    while i<4:
        print(i,end="")
        i+=1
        
    #q3

    print("hello,",'how',"""are""","you?")

    #q4

    seq ={"animals":["panda","dear","lion","eagle"],
          "counts":["10","5.23","8.0",12]
          }
    print(seq)
    l=[]
    for k,v in seq.items():
        if k =="counts":
            for i in v:
                l.append(int(float(i)))

    seq["counts"]=l
    print(seq)

    #q5
    import datetime

    print(datetime.date.today() + datetime.timedelta(days=7))
except exception as e:
  print("-----------")
