#!/usr/bin/env python3

import signal

# write a signal handler, so when you ^c it catches and will not die immediately

def ctrlc_handler(signum, frm):
    print ("Haha! You cannot kill me!")

# signal and then the handler
print ("Installing signal handler...")
signal.signal(signal.SIGINT, ctrlc_handler)
print ("Done!")

# wait on an infinaite loop
while True:
    pass

