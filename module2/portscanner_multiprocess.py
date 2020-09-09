#!/usr/bin/env python3

# multiprocessing port scanner

import socket
from multiprocessing import Pool

target = '127.0.0.1'
list1 = []

def f(port):
    s = socket.socket()
    s.settimeout(.25)
    
    try:
        con = s.connect((target,port))
        print("Success:" + str(port))
        s.close()
    except:
        print("Didn't work:" + str(port))
        s.close()
        pass

# This function creates a list to iterate thru for the map function
#def port_list1():
#    port_range = input("How many ports would you like to scan?").split(' ')
#    for val in port_range:
#        list1.append(int(val))
#    print(list1)

def port_list2():
    port_range = input("Enter the port range you want to scan ie. 1-10 ").split('-')
    for i in range(int(port_range[0]), int(port_range[1]) + 1):
        list1.append(int(i))

    #print(list1)

if __name__ == '__main__':
    port_list2()
    with Pool(2) as p:
        print(p.map(f,list1))
        print("Done")
