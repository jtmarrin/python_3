#!/usr/bin/env python3

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('localhost', username='demo', password='demoPassword')

# exec_command runs commands via ssh, can run complicated programs, send params, wahtever you want
stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd')
for line in stdout.readlines():
    print(line.strip())
ssh.close()
