#!/usr/bin/env python3

# where is fork() useful: When parent and child need to share lots of code base as well as resources

import os

# function that child process needs to execute
def child_process():
    print ("I am a child process and PID is : %d" %os.getpid())
    print ("The child is exiting:")

def parent_process():
    print ("I am the parent process with PID : %d" %os.getpid())
    childpid = os.fork()

    if childpid == 0:
        # we are inside the child
        child_process()
    else:
        # we are in the parent
        print ("We are inside the parent process")
        print ("Our child has the PID: %d" %childpid)
    while True:
        pass
parent_process()

