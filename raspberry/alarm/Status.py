#!/usr/bin/python

# start blinking led as indication the alaram system is switched on

import time
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO_blinkingLed = 26
GPIO.setup(GPIO_blinkingLed,GPIO.OUT)
GPIO.output(GPIO_blinkingLed,False)

def status():
	try:
		while(1):
			GPIO.output(GPIO_blinkingLed, True)
			time.sleep(3)
			GPIO.output(GPIO_blinkingLed, False)
			time.sleep(1)

	except KeyboardInterrupt:
		GPIO(GPIO_blinkingLed,False)
		GPIO.cleanup()
		sys.exit(0)

if __name__ == '__main__':
	status()
