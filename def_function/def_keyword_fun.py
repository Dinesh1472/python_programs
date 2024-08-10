try:
    def studentLibrary(firstname,lastname):
      print(firstname,lastname)

    studentLibrary(firstname='sam',lastname='k')

    studentLibrary(lastname='john',firstname='hary')
except Exception as e:
    print(e)
