#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

import time
# import hashlib
from utils import *
from config import *
from pyfingerprint import PyFingerprint
from pyfingerprint import FINGERPRINT_CHARBUFFER1
from pyfingerprint import FINGERPRINT_CHARBUFFER2


# Write log to txt file
def write_log(file_path, string):
    with open(file_path, 'w') as f:
        f.write(string)

def finger_enroll(index):
    ## Enrolls new finger
    ##

    ## Tries to initialize the sensor
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if (f.verifyPassword() == False):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) + '/' + str(f.getStorageCapacity()))

    ## Tries to enroll new finger
    try:
        write_log('/home/pi/build-checkFace-Desktop-Debug/log_data/notification.txt', 'Vân tay đang chờ')
        print('Waiting for finger...')

        ## Wait that finger is read

        while (f.readImage() == False):
            pass


        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(FINGERPRINT_CHARBUFFER1)

        ## Checks if finger is already enrolled
        result = f.searchTemplate()
        positionNumber = result[0]

        if (positionNumber >= 0):
            print('Template already exists at position #' + str(positionNumber))
            write_log('/home/pi/build-checkFace-Desktop-Debug/log_data/notification.txt', 'Trùng vân tay')
            # exit(0)
            return False

        print('Remove finger...')

        print('Waiting for same finger again...')

        ## Wait that finger is read again
        while (f.readImage() == False):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 2
        f.convertImage(FINGERPRINT_CHARBUFFER2)

        ## Compares the charbuffers
        if (f.compareCharacteristics() == 0):
            print('Fingers do not match')
            return False

        ## Creates a template
        f.createTemplate()

        ## Saves template at new position number

        positionNumber = f.storeTemplate(index)
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))

        return True
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        # exit(1)
        write_log('/home/pi/build-checkFace-Desktop-Debug/log_data/notification.txt', 'Có lỗi xảy ra')
        return False

    # return success



def fingerprinter_enroll(id):
    loop = 0
    while (loop < 3):
        if (finger_enroll(id) == True):
            return True
        print('Try again...1')
        time.sleep(1.5)
        loop +=1
    return False
if __name__ == '__main__':
    fingerprinter_enroll(1)