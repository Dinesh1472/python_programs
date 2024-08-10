try:
    g_str = 'hello welcome to elegant'

    print("original string is : " + g_str)
    hlf_idx = len(g_str) //2

    res = g_str[:hlf_idx] + g_str[hlf_idx:].upper()
    print("The half string : " + str(res))

except Exception as e:
    print(e)
