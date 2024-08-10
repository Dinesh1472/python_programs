/lines_perfile =10
smallfile =None
with open('dineshfile.txt')as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno %lines_perfile==0:
            if smallfile:
                smallfile.close()
            smallfilename='small_file-{}.txt'.format(lineno+lines_perfile)    
            smallfile=open(smallfilename,'w')

        smallfile.write(line)
    if smallfile:
        smallfile.close()
