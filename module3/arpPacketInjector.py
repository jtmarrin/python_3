#!/usr/bin/env python3

# ARP packet injector with raw socket

import struct
import socket

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
rawSocket.bind(("eth0", socket.htons(0x0800)))

source_mac = b'08:00:27:5e:26:c3'        # sender mac address
source_ip  = "192.168.56.101"           # sender ip address
dest_mac = b'\xbb\xbb\xbb\xbb\xbb\xbb'   # target mac address
dest_ip  = "192.168.56.103"             # target ip address

# Ethernet Header
protocol = 0x0806                       # 0x0806 for ARP
eth_hdr = struct.pack("!6s6sH", dest_mac, source_mac, protocol)

# ARP header
htype = 1                               # Hardware_type ethernet
ptype = 0x0800                          # Protocol type TCP
hlen = 6                                # Hardware address Len
plen = 4                                # Protocol addr. len
operation = 1                           # 1=request/2=reply
src_ip = socket.inet_aton(source_ip)
dst_ip = socket.inet_aton(dest_ip)
arp_hdr = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, operation, source_mac, src_ip, dest_mac, dst_ip)

packet = eth_hdr + arp_hdr
rawSocket.send(packet)