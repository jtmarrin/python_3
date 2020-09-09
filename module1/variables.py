#!/usr/bin/python3

# global var
i = 100

class PortScan:
    # class var
    default_ports = [ 21, 22, 80, 443, 8080 ]

    # initialize the class
    def __init__(self, range):
        # ports_to_scan is an instance var
        # if user assigns a range it is assigned to this instance var
        self.ports_to_scan = range

    def GetPorts(self):
        return self.ports_to_scan

class MyPortScan(PortScan):
    # overwrite GetPorts
    def GetPorts(self):
        self.ports_to_scan = [ 1, 2, 3 ]
        return self.ports_to_scan

print ("Global Variable: " + str(i))
print ("Default Ports: " + str(PortScan.default_ports))

PortScan.default_ports.append(200)
print ("Appended Default Ports: " + str(PortScan.default_ports))

newScan = PortScan([ 100, 200, 300])
print ("New Ports to scan: " + str(newScan.GetPorts()))

newMyPortScan = MyPortScan([ 100 ])
print ("Override Parent Method proof " + str(newMyPortScan.GetPorts()))

