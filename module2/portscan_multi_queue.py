#!/usr/bin/env python3

from multiprocessing import Process, Queue
from scapy.all import *
import sys
from queue import Queue as TQ

def WorkerProcess(ip, pid, q):
    while True:
        port = 0
        try:
            port = q.get(block=False)
        except TQ.empty:
                print("Worker %d exiting..." %(pid))
                return 0

        # port scanning to begin with scapy
        response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), verbose=False, timeout=.2)
        # only check for SYN?ACK flags == 18
        # filtered ports etc is another story
        if response:
            if response[TCP].flags == 18:
                print("Thread ID %d Rec's port number %d Status: OPEN" %(pid,port))

que = Queue()

for j in range(1,100):
    que.put(j)

worker_ids = []

for i in range(1, 3):
    print("Creating Worker : %d" %i)
    worker = Process(target=WorkerProcess, args=(sys.argv[1], i, que))
    worker.start()
    worker_ids.append(worker)
    print("WorkerThread %d Created!" %i)

