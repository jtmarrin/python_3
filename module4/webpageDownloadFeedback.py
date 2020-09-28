#!/usr/bin/env python3

# script to show feedback on web downloads that are large

import sys
import time
import urllib.request

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r..%d%%, %d MB, %d FB/s, %d seconds passed\n" %(percent, progress_size / (1024 * 1024),speed, duration))
    sys.stdout.flush()

def save(url, filename):
    urllib.request.urlretrieve(url, filename, reporthook)

if __name__ == "__main__":
    url = 'https://google.com'
    filename = 'google.com'
    save(url, filename)

