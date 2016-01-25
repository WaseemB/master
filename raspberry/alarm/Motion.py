#!/usr/bin/python

# pir_1.py
# Detect movement using a PIR module
#
# motion detection
# Import required Python libraries

import logging
import time
import RPi.GPIO as GPIO

from logging.handlers import RotatingFileHandler

GPIO_PIR1 = 7
GPIO_PIR2 = 8

def motion():
	Current_State = 0
	Previous_State = 0
	pir1_motion_detected = 0
	pir2_motion_detected = 0
	GPIO.setup(GPIO_PIR1, GPIO.IN)
	GPIO.setup(GPIO_PIR2, GPIO.IN)
	GPIO.setup(25,GPIO.OUT)
	GPIO.output(25,False)
	GPIO.setup(12,GPIO.OUT)
	GPIO.output(12,False)
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
  		while True :
    			# Read PIR state
			if GPIO.input(GPIO_PIR1) and pir1_motion_detected==0:
				print (time.strftime("%d/%m/%Y-%H:%M:%S   PIR1: Motion detected"))
				logger.info(time.strftime("%d/%m/%Y-%H:%M:%S   PIR1: Motion detected"))
				pir1_motion_detected=1
			if GPIO.input(GPIO_PIR2) and pir2_motion_detected==0:
				logger.info(time.strftime("%d/%m/%Y-%H:%M:%S   PIR2: Motion detected")) 
				pir2_motion_detected=1
    			Current_State = GPIO.input(GPIO_PIR1) or GPIO.input(GPIO_PIR2) 
    			if Current_State==1 and Previous_State==0:
				print (time.strftime("%d/%m/%Y-%H:%M:%S   PIR2: Motion detected"))
				logger.info(time.strftime("%d/%m/%Y-%H:%M:%S   PIR2: Motion detected"))
      				# put the led to True
				GPIO.output(25,True)
      				GPIO.output(12,True) # trigger transistor base to siren
				time.sleep(2) ### time for siren on
      				GPIO.output(25,False)
				GPIO.output(12,False)
      				# Record previous state
      				Previous_State=1
    			elif Current_State==0 and Previous_State==1:
      				# PIR has returned to ready state
      				Previous_State=0
				pir1_motion_detected=0
				pir2_motion_detected=0            
      
	except KeyboardInterrupt:
		sys.exit(0)
	except:
		print "All other errors"
  	finally:
		GPIO.cleanup()
		print "*** PIR Cleanup Done! ***\n"
