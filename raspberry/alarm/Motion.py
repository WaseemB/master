#!/usr/bin/python

# pir_1.py
# Detect movement using a PIR module
#
# motion detection
# Import required Python libraries

import sys
import time
import RPi.GPIO as GPIO

GPIO_PIR = 7

def motion():
	Current_State = 0
	Previous_State = 0
	GPIO.setup(GPIO_PIR, GPIO.IN)
	GPIO.setup(25,GPIO.OUT)
	GPIO.output(25,False)
	GPIO.setup(12,GPIO.OUT)
	GPIO.output(12,False)
	
	try:
		print "Waiting for PIR to settle ..."
  		time.sleep(10)
  		print "  Ready"
  
  		# Loop until users quits with CTRL-C
  		while True :
    			# Read PIR state
    			Current_State = GPIO.input(GPIO_PIR)
    			if Current_State==1 and Previous_State==0:
      				# PIR is triggered
      				print (time.strftime("%d/%m/%Y-%H:%M:%S Motion detected"))
      				# put the led to True
				GPIO.output(25,True)
      				GPIO.output(12,True) # trigger transistor base to siren
				time.sleep(1) ### time for siren on
      				GPIO.output(25,False)
				GPIO.output(12,False)
      				# Record previous state
      				Previous_State=1
    			elif Current_State==0 and Previous_State==1:
      				# PIR has returned to ready state
      				Previous_State=0            
      
	except KeyboardInterrupt:
		sys.exit(0)
	except:
		print "All other errors"
  	finally:
		GPIO.cleanup()
		print "*** PIR Cleanup Done! ***\n"
