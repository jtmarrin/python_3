#!/usr/bin/env python3

# print file stats for file entered into the command line

import sys, os, time
import pwd # password db module
from stat import * # ST_SIZE etc

file = sys.argv[1]

try:
    st = os.stat(file)
except IOError:
    print("Failed to get info about ", file)
else:
    print ("Owner: uid is %d, username is %s" %(st.st_uid, pwd.getpwuid(st.st_uid).pw_name))
    print ("file size:", st[ST_SIZE])
    print ("file modified:",time.asctime(time.localtime(st[ST_MTIME])))
    print ("File accessed time:",time.asctime(time.localtime(st[ST_ATIME])))
    print ("File changed time:",time.asctime(time.localtime(st[ST_CTIME])))
    print ("File mode:",(st[ST_MODE]))
