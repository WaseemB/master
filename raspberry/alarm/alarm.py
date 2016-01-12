#!/usr/bin/python

import threading
import time

import Door
import Motion


results = {}

def get_a():
    results['a'] = Door.door()
a_thread = threading.Thread(target=get_a)
a_thread.start()

def get_b():
    results['b'] = Motion.motion()
b_thread = threading.Thread(target=get_b)
b_thread.start()

a_thread.join()
b_thread.join()

