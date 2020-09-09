#!/usr/bin/env python3

import threading
import time

def worker_thread(id):
    print ("Thread with ID: %d is alive" %id)
    count = 1
    while True:
        print ("Thread with ID: %d has counter value %d" %(id,count))
        time.sleep(2)
        count += 1
        
for i in range(5):
    x = threading.Thread(target=worker_thread, args=(i,))
    x.start()

print ("main thread going for an infinate wait loop")
while True:
    pass
