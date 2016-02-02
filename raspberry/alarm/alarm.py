#!/usr/bin/python

#import threading
import multiprocessing

import Door
import Motion

results = {}

def get_a():
    results['a'] = Door.door()
def get_b():
    results['b'] = Motion.motion()
	
a_process = multiprocessing.Process(target=get_a)
b_process = multiprocessing.Process(target=get_b)

a_process.start()
b_process.start()

a_process.join()
b_process.join()
