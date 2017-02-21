#!/usr/bin/python

# heartbeat.py
# Send heartbeat message
#
# Import required Python libraries

#import fcntl
#import logging
#import signal
import time
import os
import sys

def heartbeat():

	#try:
		# Loop until users quits with CTRL-C
	
	while(1):
				  			
	#		try:
		os.system("./heartbeatAlert.py")				
		time.sleep(14400) # wait once every 8 hours
			#except:
			#	print "Unexpected heartbeat error"
#except KeyboardInterrupt:
#	sys.exit(0)

if __name__ == '__main__':
		heartbeat()
