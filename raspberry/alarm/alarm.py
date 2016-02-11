#!/usr/bin/python

#import threading
import multiprocessing

import Door
import Motion
import Status

results = {}

def get_a():
    results['a'] = Door.door()
def get_b():
    results['b'] = Motion.motion()
def get_c():
    results['c'] = Status.status()
	
a_process = multiprocessing.Process(target=get_a)
b_process = multiprocessing.Process(target=get_b)
c_process = multiprocessing.Process(target=get_c)

a_process.start()
b_process.start()
c_process.start()

a_process.join()
b_process.join()
c_process.join()