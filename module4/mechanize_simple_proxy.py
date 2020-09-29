#!/usr/bin/env python3

# apt-get install tinyproxy -- runs by default on 8888
# simple mechanize proxy
# run ./meachanize_simple_proxy.py localhost 8888

import mechanize
import sys

browser = mechanize.Browser()
browser.set_proxies({'http' : sys.argv[1] + ':' + sys.argv[2]})
browser.open('http://securitytube.net')

for form in browser.forms():
    print(form)
