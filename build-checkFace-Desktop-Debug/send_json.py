import json
import requests
import shutil
import datetime
import time
import os
dt = datetime.datetime.today()

origin_file = 'log_data/checkin.json'
file_to_send = '/time_logs/'+str(dt.day)+'-'+str(dt.month)+'-'+str(dt.year)+'.json'
# file_to_send = '/home/pi/build-checkFace-Desktop-Debug/time_logs/'+str(time.ctime())+'.json'
# if not os.path.exists(file_to_send):
#     os.makedirs(file_to_send)
print(file_to_send + ' is created!')

shutil.copy(origin_file, file_to_send)

dir_file_to_sent = 'time_logs/'

def listfiles(rootdir):
    files = []
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        files.append(d)
    return files

listfiles = listfiles(dir_file_to_sent)
# print(listfiles)

def clear_json(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        data['data'] = []

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

### SEND JSON DATA
# # JSON file
# with open('/home/pi/build-checkFace-Desktop-Debug/log_data/checkin.json') as json_file:
#     json_data = json.load(json_file)
#
# # print(json_data)
#
# r = requests.post('http://172.20.30.178:5000/get_json_data', json=json_data)
# print(r.text)

### SEND JSON FILE

def send_json(data_file):

    url = "http://172.20.40.35:6667/get_json"

    files = [
        ('document', (data_file, open(data_file, 'rb'), 'application/octet')),
    ]

    r = requests.post(url, files=files)
    message = str(r.content, 'utf-8')
    print(message)
    clear_json(origin_file)
    if message == 'success':
        os.remove(data_file)

for i in range(len(listfiles)):
    send_json(listfiles[i])


