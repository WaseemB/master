#!/usr/bin/python

import os

SENDMAIL = "/usr/sbin/sendmail" # sendmail location

FROM = "raspberrypi-004"
#TO = ["waseem.besada@gmail.com"]
TO = ["waseem@telia.com"]

SUBJECT = "PIR1 motionAlarm!"

TEXT = "**** sendMail.py - PIR1 Alarm This message was sent via sendmail.****"

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
