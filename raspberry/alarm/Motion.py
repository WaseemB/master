#!/usr/bin/python

# pir_1.py
# Detect movement using a PIR module
#
# motion detection
# Import required Python libraries

import logging
import time
import os
import sys

#import motionAlarmPIR1
#import motionAlarmPIR2

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

from logging.handlers import RotatingFileHandler

GPIO_PIR1 = 7
GPIO_PIR2 = 8

def motion():
	GPIO.setup(GPIO_PIR1, GPIO.IN)
	GPIO.setup(GPIO_PIR2, GPIO.IN)
	GPIO.setup(25,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)
	"""
    	Creates a rotating log
    	"""
	logger = logging.getLogger("Rotating Log")
	logger.setLevel(logging.INFO)	
	
	# add a rotating handler
	handler = RotatingFileHandler("motion.log", maxBytes=200000,backupCount=5)
	logger.addHandler(handler)
	
	try:
		print "Waiting for PIR to settle ..."
  		time.sleep(10)
  		print "  Ready"
  
  		# Loop until users quits with CTRL-C
  		while(1):
			GPIO.output(12,False)
			GPIO.output(25,False)
			pir1_motion_detected = 0
			pir2_motion_detected = 0
			Previous_State = 0
    			# Read PIR state
			if GPIO.input(GPIO_PIR1) and pir1_motion_detected==0:
				print (time.strftime("%d/%m/%Y-%H:%M:%S   PIR1: Motion detected"))
				logger.info(time.strftime("%d/%m/%Y-%H:%M:%S   PIR1: Motion detected"))
				pir1_motion_detected=1
				os.system("./motionAlarmPIR1.py")
			if GPIO.input(GPIO_PIR2) and pir2_motion_detected==0:
				print (time.strftime("%d/%m/%Y-%H:%M:%S   PIR2: Motion detected"))
				logger.info(time.strftime("%d/%m/%Y-%H:%M:%S   PIR2: Motion detected")) 
				pir2_motion_detected=1
				os.system("./motionAlarmPIR2.py") 
			if pir1_motion_detected==1 or pir2_motion_detected==1:
      				# put the led to True
				GPIO.output(25,True)
      				GPIO.output(12,True) # trigger transistor base to siren
				time.sleep(2) ### time for siren on
          
	except KeyboardInterrupt:
		GPIO.output(25,False)
		GPIO.output(12,False)
		GPIO.cleanup()
		sys.exit(0)
