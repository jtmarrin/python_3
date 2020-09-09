#!/usr/bin/env python3

# If there is a robots.txt file for a website, we will check for Disallow tag and raise an exception
# create class with baseclass Exception

import urllib3
import certifi

class DisallowPresent(Exception):
    def __init__(self, path):
        self.disallow_path = path
    def __str__(self):
        return repr(self.disallow_path)

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
r = http.request('GET', 'https://cnn.com/robots.txt')
for line in r.data:
    try:
        if line.lower().find('disallow') != -1:
            print (line.strip())
            # split and take second elemet and strip new line
            raise DissallowPresent(line.split(':')[1].strip())
    except DisallowPresent as ex:
        # printing Exception with disallowed path which is from the instance variable
        print ("Exception occured for path: " + str(ex.disallow_path))
