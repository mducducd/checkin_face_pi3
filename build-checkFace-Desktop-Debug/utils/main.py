open('/home/pi/build-checkFace-Desktop-Debug/log_data/notification.txt', 'w').close
from config import *

with open(notification_file, 'w') as f:
    f.write(startup)
print('Warming up')
import time
start_time = time.time()
from register import register
from facerec import facerec, facerec_api
from finger_search import finger_search
print('Time Start up: '+str(time.time()-start_time))

def deploy(mode):
    if mode == 0:
        facerec()
    if mode == 1:
        register()
    if mode == 2:
        finger_search()

while True:
    time.sleep(0)
    duc = open('/home/pi/build-checkFace-Desktop-Debug/log_data/switch.txt', 'r')
    mode = int(duc.read())
    deploy(mode)
    

