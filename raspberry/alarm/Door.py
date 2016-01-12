#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
# 
# control the status of door switch, and the green and yellow led
 
# GPIO 23 set up as input. It is pulled up to stop false signals

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(17,False)
GPIO.output(27,False)

def door():
	GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	#print "Make sure you have a button connected so that when pressed"
	#print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"
	#raw_input("Press Enter when ready\n>")

	print "Waiting for falling edge on port 23"
	# now the program will do nothing until the signal on port 23 
	# starts to fall towards zero. This is why we used the pullup
	# to keep the signal high and prevent a false interrupt

	#print "During this waiting time, your computer is not" 
	#print "wasting resources by polling for a button press.\n"
	#print "Press your button when ready to initiate a falling edge interrupt."
	try:
		while True:
    			GPIO.wait_for_edge(23, GPIO.FALLING)
			print "door close"
			GPIO.output(17,True)
			GPIO.output(27,False)
			GPIO.wait_for_edge(23, GPIO.RISING)
                	print "door open"
                	GPIO.output(17,False)
                	GPIO.output(27,True)
    			#print "\nFalling edge detected. Now your program can continue with"
    			#print "whatever was waiting for a button press."
	except KeyboardInterrupt:
		GPIO(17,False)
		GPIO(27,False)
		GPIO(23,False)  ## not sure if this is possible
	finally:
		print "\n\ncleaning up!\n"
		GPIO.cleanup()           # clean up GPIO on CTRL+C exit
		print "*** Done! ***\n"
