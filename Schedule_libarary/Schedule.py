#schedule Library imported
import schedule
import time

try:
    #Functions setup
    def sudo_placement():
        print('get ready for sudo placement at geeksfor geeks')

    def good_luck():
        print('Good Luck for test')

    def work():
        print('study and work hand')

    def bedtime():
        print('It is bed time go rest')

    def geeks():
        print('Shaurya says geeksforgeeks')


    #task scheduling
    #After every 10mins geeks()is called
    schedule.every(1).minutes.do(geeks)

    #After every hours geeks()is called
    schedule.every().hour.do(geeks)

    #Every day at 12am or 00:00 time bedtime()is called
    schedule.every().day.at("00:00").do(bedtime)

    #After every 5 to 10mins in between run work()
    schedule.every(5).to(10).minutes.do(work)

    #Every monday good-luck()is called
    schedule.every().monday.do(good_luck)

    #Every tuesday at 18:hours sudo-placement()is called
    schedule.every().tuesday.at('18:00').do(sudo_placement)

    #Loops so that the scheduling task
    #Keeps on running time
    while True:
        #Checks whether a scheduled task
        #is pending to run or not
        schedule.run_pending()
        time.sleep(1)

except Exception as e:
    print(e)
