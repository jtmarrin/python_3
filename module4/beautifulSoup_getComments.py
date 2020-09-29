#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request

htmlPage = urllib.request.urlopen("http://www.securitytube.net/video/7313")
htmlDom = BeautifulSoup(htmlPage)
allComments = htmlDom.find_all("ul", class_="comments")
print(allComments[0].get_text())

