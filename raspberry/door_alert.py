# control the yellow led
import RPi.GPIO as GPIO
import re
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)

door_alert_on = False
alarm = False

sys.stdout.write('Start door_alert [Yes/No] ')
doStart = sys.stdin.readline()
result = bool('Yes' in doStart)
if result:
	door_alert_on = True
	GPIO.output(22,True)
## put interupt2 here 
else:
	GPIO.output(22,False)
	exit(0)

	
raw_input("Press Enter when ready\n>")
if door_alert_on:
	GPIO.output(22,False)
	


