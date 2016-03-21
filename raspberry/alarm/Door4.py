#!/usr/bin/bython

# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
# 
# control the status of door switch, and the green and yellow/red led
 
# GPIO 21 set up as input. It is pulled up to stop false signals


import logging
import signal
import os
import sys
import time
import RPi.GPIO as GPIO
from logging.handlers import RotatingFileHandler

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(17,True) # initiallt the Door should be closed
GPIO.output(27,False)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

"""
Creates a rotating log
"""
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)	

# add a rotating handler
handler = RotatingFileHandler("door.log", maxBytes=200000,backupCount=5)
logger.addHandler(handler)

GPIO.add_event_detect(21,GPIO.BOTH, bouncetime=1000)

logger.info(time.strftime("%d/%m/%Y %H:%M:%S === Door alarm started ==="))
print (time.strftime("%d/%m/%Y %H:%M:%S === Door alarm started ==="))
print  (time.strftime("%d/%m/%Y %H:%M:%S Door closed"))
print  "Waiting for door trigger"

def is_false_positive():
	print (time.strftime("%d/%m/%Y %H:%M:%S is_false_positive called"))
	time.sleep(0.01)
	if GPIO.input(21) != GPIO.HIGH:
		print (time.strftime("%d/%m/%Y %H:%M:%S interferance occured"))
		return True
	else:
		return False

def doorAlarm():		
	try:
		while(1):
				GPIO.wait_for_edge(21, GPIO.RISING)    			
				if is_false_positive() is False:			
					logger.info(time.strftime("%d/%m/%Y %H:%M:%S Door opened"))
					print (time.strftime("%d/%m/%Y %H:%M:%S Door opened"))
					os.system("./doorAlertOpened.py")
					GPIO.output(17,False)
					GPIO.output(27,True)
					time.sleep(0.1)
					GPIO.wait_for_edge(21, GPIO.FALLING)
					logger.info(time.strftime("%d/%m/%Y %H:%M:%S Door closed"))
                			print (time.strftime("%d/%m/%Y %H:%M:%S Door closed"))
					os.system("./doorAlertClosed.py")
                			GPIO.output(17,True)
                			GPIO.output(27,False)
					time.sleep(0.1)

	except KeyboardInterrupt:
		GPIO.output(17,False) #exit on CTRL+C
		GPIO.output(27,False)
		GPIO.cleanup()
		sys.exit(0)

if __name__ == '__main__':
	doorAlarm()
