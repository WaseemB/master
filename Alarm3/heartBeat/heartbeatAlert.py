#!/usr/bin/python

import os
import time

SENDMAIL = "/usr/sbin/sendmail" # sendmail location

FROM = "raspberrypi-064" # IP 192.168.1.2
TO = ["waseem.besada@gmail.com"]
#TO = ["waseem@telia.com"]

SUBJECT = "heartbeatAlert!"

TEXT = time.strftime("%d/%m/%Y-%H:%M:%S")+"   heartbeatAlert from raspberrypi-064 192.168.1.2" # + "os.system("/opt/vc/bin/vcgencmd measure_temp")  

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
p = os.popen("%s -t -i" % SENDMAIL, "w")
p.write(message)
status = p.close()
if status:
    print "Sendmail exit status", status
