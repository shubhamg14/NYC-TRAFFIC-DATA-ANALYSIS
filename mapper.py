#!/usr/bin/env python
import sys
import csv

# input comes from STDIN (standard input)
reader=csv.reader(sys.stdin,delimiter=',')
#Ignoring Header
reader.next()
for line in reader:
	for word in line[24:29]:
		if word.strip():
    # remove leading and trailing whitespace
			word = word.strip()
    # increase counters
	 # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
			print '%s\t%s' % (word.lower(), 1)
