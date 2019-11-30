#!/usr/bin/python

# pir_1.py
# Detect movement using a PIR module
#
# motion detection (pir2)
# Import required Python libraries

import fcntl
import logging
import signal
import time
import os
import sys
from datetime import date,datetime
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

from logging.handlers import RotatingFileHandler
#today = str(date.today())
GPIO_PIR2 = 8
GPIO.setup(8, GPIO.IN,  pull_up_down=GPIO.PUD_UP)

GPIO.setup(12,GPIO.OUT) # transistor base (siren)
GPIO.setup(25,GPIO.OUT) # Red Led	
siren_on = False

GPIO.setup(GPIO_PIR2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(GPIO_PIR2,GPIO.BOTH, bouncetime=1000)

#Creates a rotating log
 
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)	
	
# add a rotating handler
handler = RotatingFileHandler("/var/www/html/motion2.log", maxBytes=200000,backupCount=5)
logger.addHandler(handler)
	
def is_false_positive():
#	logger.info(time.strftime("%d/%m/%Y %H:%M:%S   PIR2 is_false_positive called"))
#	print (time.strftime("%d/%m/%Y %H:%M:%S   PIR2 is_false_positive called"))
	time.sleep(0.1)	
	if GPIO.input(8) != GPIO.HIGH:
#		logger.info(time.strftime("%d/%m/%Y %H:%M:%S   PIR2 interferance occured"))
#		print (time.strftime("%d/%m/%Y %H:%M:%S   PIR2 interferance occured"))
		return True
	else:
		return False
	
def motion():
	try:
		print "Waiting for PIR2 to settle ..."
  		time.sleep(20) # 30~60 sec to stabilize the sensor and avoid unstable state
  		print (time.strftime("%d/%m/%Y-%H:%M:%S   PIR2 Ready"))
  
  		# Loop until users quits with CTRL-C
		while(1):
				
			#if siren_on is False:
			#	siren_on = True   
			#	GPIO.output(25,True) # Red Led   			
			#	GPIO.output(12,True) # trigger transistor base to siren
			try:
				GPIO.output(12,False)
				GPIO.output(25,False)
				GPIO.wait_for_edge(GPIO_PIR2,GPIO.RISING)	
				if is_false_positive() is False:		
					print (time.strftime("%d/%m/%Y-%H:%M:%S   PIR2: Motion detected"))
					logger.info(time.strftime("%d/%m/%Y-%H:%M:%S   PIR2: Motion detected"))
					if str(str(date.today())) < ('2019-11-04'):
						os.system("./motionAlertPIR2.py")		
						if GPIO.input(12) == 0:				
							myfile = open("/var/www/html/motion2.log", "ab")
							fcntl.flock(myfile, fcntl.LOCK_EX)				
							myfile.write(time.strftime("%d/%m/%Y-%H:%M:%S   PIR2: siren on \n"))
							GPIO.output(25,True) # Red Led
							GPIO.output(12,True) # trigger transistor base to siren
							time.sleep(8) # time for siren
							fcntl.flock(myfile, fcntl.LOCK_UN)
							myfile.close()
			except IOError:
				print 'cannot open file'
				GPIO.output(25,False)
				GPIO.output(12,False)
			except:
				print "Unexpected error"
				GPIO.output(25,False)
				GPIO.output(12,False)
				raise 
				GPIO.output(25,False)
				GPIO.output(12,False)

	except KeyboardInterrupt:
		GPIO.output(25,False)
		GPIO.output(12,False)
		GPIO.cleanup()
		sys.exit(0)

if __name__ == '__main__':
	motion()
