try:
    list=['jan','feb','mar','april','may','jun','july','aug','sep','oct','nov','dec']

    for emonth in list:
        if emonth.startswith('j'):
          print(emonth)
except Exception as e:
    print(e)
 
