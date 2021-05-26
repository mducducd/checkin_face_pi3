import os
import tqdm
from annoy import AnnoyIndex
import time
import numpy as np
from utils.pyfingerprint import PyFingerprint

#generate annoy tree
NUMBER_OF_TREES = 5000
f = 128
t = AnnoyIndex(f, 'euclidean')

def listdirs(rootdir):
    rootdirs = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            listdirs(d)
            rootdirs.append(d)
    return rootdirs

def listfiles(rootdir):
    files = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)

        files.append(d)
    return files

dirpaths = listdirs('encode')

file1 = open("hyper_id1.txt", "w")
count = -1
for imagePaths in dirpaths:
    dirnames = os.path.basename(imagePaths)
    imagePaths = listfiles(imagePaths)
    for i, imagePath in tqdm.tqdm(enumerate(imagePaths)):
        if (".txt" in imagePath):
            filename11 = os.path.basename(imagePath)
            filename11 = filename11.replace(".txt","")
            # use directory name for person id
            file1.write(dirnames)
            file1.write("\n")
            with open(imagePath, 'r') as file_in:

                lines = []
                for line in file_in:
                    line = line.replace("\n","")
                    line = float(line)
                    lines.append(line)
                lines = np.array(lines)
                count += 1
            #add to tree
            t.add_item(count, lines)
t.build(NUMBER_OF_TREES,-1)

t.save(r'all_hyper1.ann')

## Deletes a finger from sensor
##


# Tries to initialize the sensor
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

## Tries to delete the template of the finger
try:
    # positionNumber = input('Please enter the template position you want to delete: ')
    # positionNumber = int(positionNumber)
    # temps_num = f.getTemplateCount()
    # positionNumber= len(os.listdir('/home/pi/build-checkFace-Desktop-Debug/encode'))
    # f.deleteTemplate(positionNumber, temps_num-positionNumber)
    #     print('Template deleted!')
    f.clearDatabase()
except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
