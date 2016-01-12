#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# pir_1.py
# Detect movement using a PIR module
#
# Author : Matt Hawkins
# Date   : 21/01/2013

# Import required Python libraries
#
# motion detection

import time
import RPi.GPIO as GPIO

GPIO_PIR = 7

def motion():
	Current_State = 0
	Previous_State = 0
	GPIO.setup(GPIO_PIR, GPIO.IN)
	GPIO.setup(8,GPIO.OUT)

	try:

		print "Waiting for PIR to settle ..."
  		time.sleep(10)

  		# Loop until PIR output is 0
  		while GPIO.input(GPIO_PIR)==1:
    			Current_State  = 0
  		print "  Ready"
  
  		# Loop until users quits with CTRL-C
  		while True :
    			# Read PIR state
    			Current_State = GPIO.input(GPIO_PIR)
    			if Current_State==1 and Previous_State==0:
      				# PIR is triggered
      				print (time.strftime("%d/%m/%Y"))
      				print (time.strftime("%H:%M:%S"))
      				GPIO.output(8,True)
      				print "  Motion detected!"
      				time.sleep(1)
      				GPIO.output(8,False)
      				print "------------------"
      				# Record previous state
      				Previous_State=1
    			elif Current_State==0 and Previous_State==1:
      				# PIR has returned to ready state
      				print "  Ready"
      				Previous_State=0
      
    				# Wait for 1000 milliseconds
    				time.sleep(1)      
      
	except KeyboardInterrupt:
  		print "  Quit" 
  	# Reset GPIO settings
  	GPIO.cleanup()
