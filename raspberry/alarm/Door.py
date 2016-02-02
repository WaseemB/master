# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
# 
# control the status of door switch, and the green and yellow/red led
 
# GPIO 23 set up as input. It is pulled up to stop false signals


import logging
import signal
import os
import sys
import time

import RPi.GPIO as GPIO

from logging.handlers import RotatingFileHandler

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(17,False)
GPIO.output(27,False)

def door():
	"""
	Creates a rotating log
    	"""
	logger = logging.getLogger("Rotating Log")
	logger.setLevel(logging.INFO)	
	
	# add a rotating handler
	handler = RotatingFileHandler("door.log", maxBytes=200000,backupCount=5)
	logger.addHandler(handler)
	
	
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	print "Waiting for falling edge on port 23"
	
	try:
		while(1):
    			GPIO.wait_for_edge(23, GPIO.FALLING)
			logger.info(time.strftime("%d/%m/%Y %H:%M:%S  Door close"))
			print (time.strftime("%d/%m/%Y %H:%M:%S   Door close"))
			GPIO.output(17,True)
			GPIO.output(27,False)
			GPIO.wait_for_edge(23, GPIO.RISING)
			logger.info(time.strftime("%d/%m/%Y %H:%M:%S  Door open"))
                	print (time.strftime("%d/%m/%Y %H:%M:%S   Door open"))
			os.system("./doorAlert.py")
                	GPIO.output(17,False)
                	GPIO.output(27,True)
    			
	except KeyboardInterrupt:
		GPIO.output(17,False)
		GPIO.output(27,False)
		GPIO.cleanup()
		sys.exit(0)

