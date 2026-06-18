#!/usr/bin/env python

import sys

count = 0
total = 0
previous_key = None

for line in sys.stdin:

    data = line.strip().split("\t")
    key, value = data

    if previous_key != None and previous_key != key:
        average = total / count
        sys.stdout.write("{0}\t{1}\n".format(previous_key, round(average, 2)))
        count = 0
        total = 0

    count += 1
    total += float(value)
    previous_key = key

average = total / count
sys.stdout.write("{0}\t{1}\n".format(previous_key, round(average, 2)))
