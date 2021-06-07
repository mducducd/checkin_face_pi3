#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

import hashlib
import time
from utils import *
from config import *
from pyfingerprint import PyFingerprint
from pyfingerprint import FINGERPRINT_CHARBUFFER1

def fingerprinter_search():
    ## Search for a finger
    ##

    ## Tries to initialize the sensor
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to search the finger and calculate hash
    try:
        write_log(notification_file, fingerprint_ready)
        print('Waiting for finger...')

        ## Wait that finger is read
        timeout = time.time() + 10
        while ( f.readImage() == False and time.time()<timeout ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(FINGERPRINT_CHARBUFFER1)

        ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]

        if ( positionNumber == -1 ):
            print('No match found!')

            success = False
            # exit(0)
        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))
            success = True
            camera = Pi_Cam('fingerprint')
            camera.start_preview()
            camera.overlay_image('/home/pi/build-checkFace-Desktop-Debug/'+Data_dir+'/{}/{}.jpg'.format(positionNumber,positionNumber))
            write_log(notification_file, 'ID: {}'.format(positionNumber))
            time.sleep(3)
            # write_log(notification_file, back)
            # write_log(switch_file, '0')
            camera.stop_preview()
            camera.close()

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        success = False
        # exit(1)

    return success

def finger_search():
    loop = 0
    while loop < 4:
        if (fingerprinter_search()==True):
            break
        if loop < 3:
            write_log(notification_file, nomatch)
        print('Try again...1')
        time.sleep(1)
        delete_content(notification_file)
        loop +=1
    write_log(notification_file, back)
    write_log(switch_file, '0')

if __name__ == '__main__':
    finger_search()
