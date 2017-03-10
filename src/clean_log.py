import time
from datetime import datetime, deltatime
import json
import thread
from threading import Timer



def event(log_file):
	file_handle = open(log_file, 'w').close()

def schedule_event(log_file, time):
	perform_in = time.second
	timer = Timer(perform_in, event(log_file))
	timer.start()


if '__name__' == '__main__':
	log_file = 'data.txt'
	time = time.now().hour + 2
	schedule_event(log_file, time)










