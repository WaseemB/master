#!/usr/bin/python

import os
import time

SENDMAIL = "/usr/sbin/sendmail" # sendmail location

FROM = "raspberrypi"
TO = ["waseem.besada@gmail.com"]
#TO = ["waseem@telia.com"]

SUBJECT = "Raspberry Door Opened Alarm!"

TEXT = time.strftime("%d/%m/%Y-%H:%M:%S")+"   Door Opened Alarm!"

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
