import re
import traceback
try:
    def find_all_urls():
        fobj = open('google_viewpage.txt','r')
        fobj1 = open('result_data_19_04.txt','w')
        str = fobj.read()
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
        print (urls)
        urls = [ url+'\n' for url in urls]
        fobj1.writelines(urls)
        #for url in urls:
        #  print (url)
        fobj.close()
        fobj1.close()

    find_all_urls()

except Exception as e:
    print(e)
