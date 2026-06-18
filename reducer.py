#!/usr/bin/env python

import sys

count = 0
previous_key = None

for line in sys.stdin:

    data = line.strip().split("\t")
    key, value = data

    if previous_key != None and previous_key != key:
        if count > 114:
            sys.stdout.write("{0}\t{1}\n".format(previous_key, count))
        count = 0

    count += 1
    previous_key = key

if count > 114:
    sys.stdout.write("{0}\t{1}\n".format(previous_key, count))
