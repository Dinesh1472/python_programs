try:
        string = ['python2', 'elegant4', 'service23','worlds']
        print(string)
        # empty list
        empty = []

        for a in range(len(string)):
                empty.append(''.join(e for e in string[a] if e.isalpha()))
                             
        print(" Remove digit in the list:", empty)

except Exception as e:
        print(e)
