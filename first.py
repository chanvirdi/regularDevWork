#!/usr/bin/python

import re

a = "Hello, I'm Chanpreet"

checkReg = re.compile("^Hello.*\s(\S+)")

match = checkReg.match(a)

if match:
	print "This is working "+match.group(1) + " good to move ahead."
else:
	print "It ain't working."