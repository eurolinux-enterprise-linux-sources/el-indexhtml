#!/usr/bin/python
"""Removes last <li> from HTML file"""

import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]

with open(filename, 'r') as fd:
    soup = BeautifulSoup(fd.read(), features="html.parser")

# remove last li tag with valid community list link
if (soup('li')):
    soup('li')[-1].extract()

with open(filename, 'w') as fd:
    fd.write(soup.prettify('utf8'))
