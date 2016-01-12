#!/usr/bin/python

import threading
import time

import Door
import Motion

results = {}

def get_a():
    results['a'] = Door.door()

def get_b():
    results['b'] = Motion.motion()
	
a_thread = threading.Thread(target=get_a)	
b_thread = threading.Thread(target=get_b)

a_thread.start()
b_thread.start()
a_thread.join()
b_thread.join()

