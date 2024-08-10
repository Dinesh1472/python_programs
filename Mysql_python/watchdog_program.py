#Program to monitor a netwrok share location and if any zero byte file comes to that location
#move to a different directory

#check location existance and monitor required file is there or not. if required provide a time delay.
#if file found then send to the other bucket
#One scenario Zero byte file and other size type of files to another location
#if no files found then trigger

import os
import shutil
import time
import smtplib, ssl
import config_monitor

def directoryMonitor():

    monitorLoc = config_monitor.monitorLoc
    zeroByteLoc  = config_monitor.zeroByteLoc
    if not os.path.isdir(zeroByteLoc):
        os.makedirs(zeroByteLoc)
    arcLoc = config_monitor.arcLoc
    if not os.path.isdir(arcLoc):
        os.makedirs(arcLoc)

    while True:
        try:
            fileList = [os.path.join(monitorLoc,eFile) for eFile in os.listdir(monitorLoc) if os.path.isfile(os.path.join(monitorLoc,eFile))]
            print (fileList)
            if len(fileList):
                print ("File Segregation started")
                for eItem in fileList:
                    if os.path.getsize(eItem)>0:
                        shutil.move(eItem,arcLoc)
                    else:
                        shutil.move(eItem,zeroByteLoc)
            else:
                print ("waiting for files to reach on this location:",monitorLoc)
                sendEmail()
                time.sleep(60)

        except Exception as e:
            print (e)

def sendEmail():
    smtp_server = "mail.quintuslabs.in"
    port = 465  # For starttls
    sender_email = "support@quintuslabs.in"
    receiver_email = "sangram.bng@gmail.com"
    password = "Password@123"
    message = """\
    Subject: Hi there

    This message is sent from Python."""
    print (message)
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


directoryMonitor()