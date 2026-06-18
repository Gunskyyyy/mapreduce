#!/usr/bin/env python

import sys

# Sum of all sales (values) is initialized with zero, we just started
count = 0

# Previous key is initialized with None, we just started
previous_key = None

# For each new line in the standard input
for line in sys.stdin:

    # split the line at the tabulator ("\t")
    data = line.strip().split("\t")

    # Store the 2 elements of this line in seperate variables
    key, value = data

    # Do we have a previous_key and is the new key different than the previous key?
    if previous_key != None and previous_key != key:
        sys.stdout.write("{0}\t{1}\n".format(previous_key, count))
        count = 0

    # Add 1 to the count
    count += 1
    previous_key = key

# write the last result to stdout
sys.stdout.write("{0}\t{1}\n".format(previous_key, count))
