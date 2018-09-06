import os
import datetime
from python_serverchan import ServerChan
from python_serverchan import PushBear


serverchan = ServerChan('SCU15497Tf744a6126a8d5b36462083165eb47d8d5b8fc5f312469')
file_dir=u"/home/homeassistant/.homeassistant/www/"
list=os.listdir(file_dir)
list.sort(key=lambda fn: os.path.getmtime(file_dir+fn) if not os.path.isdir(file_dir+fn) else 0)
d=datetime.datetime.fromtimestamp(os.path.getmtime(file_dir+list[-1]))
for item in list[:-2]:
    if item[-3:] == 'gif':
        os.remove(file_dir+item)
timestp = datetime.datetime.now()
title = 'EntryCam Alert'
message = 'Motion detected![logo](https://www.beardog.top:8123/local/' + list[-1] + ')'
sendtitle = '{} {}'.format(timestp.strftime('%Y%m%d'), title)
send_message = '{} {}'.format(timestp.strftime("%Y-%m-%d %H:%M:%S"), message)
#response = serverchan.send(sendtitle, send_message)
#print(response)
pushbear = PushBear('1332-6cd56b54c9ac37c7eb2aeb4ec956eb76')
response = pushbear.send(sendtitle, send_message)
print(response)