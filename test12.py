import os

path = 'D:/FanQ'
print(os.path.exists(path))

if not os.path.exists(path):
    print('mkdir ' + path)
    os.mkdir(path)

import time
timestr = time.strftime("%Y%m%d-%H:%M:%S")
print (timestr)