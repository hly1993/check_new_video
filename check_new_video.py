import os
import time
import datetime
TIMESTAMP="%Y%m%d%H%M%S"
timestp = datetime.datetime.now()
fname = '/home/pi/tmp/tmp.txt'
os.system("sudo curl -s -u username:password http://192.168.1.*:*/sd/%s/record000/ -o /home/pi/tmp/tmp.txt" % timestp.strftime('%Y%m%d'))
with open(fname, 'r') as f:
    lines = f.readlines()
    last_line = lines[-2]
    start_str='a href="'
    s=last_line.find(start_str)
    substr=last_line[s+8:s+56]
    if substr[-10:-4]=='999999':
        last_line = lines[-3]
        start_str='a href="'
        s=last_line.find(start_str)
    videotime='20'+last_line[s+32:s+38]+last_line[s+39:s+45]
    videotimestamp = time.mktime(time.strptime(videotime,TIMESTAMP))
    nowtimestamp = time.mktime(time.strptime(timestp.strftime('%Y%m%d%H%M%S'),TIMESTAMP))
    if nowtimestamp-videotimestamp <60:
        print 1
    else:
        print 0
       
