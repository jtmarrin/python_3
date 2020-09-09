#!/usr/bin/env python3

import modules

print ('Quick Add a+b: %d' %modules.quickAdd(10,20))

# call class from module:

ins = modules.Scientific(5,6)
print ('%d' %ins.power())

