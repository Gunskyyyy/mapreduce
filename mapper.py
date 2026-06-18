#!/usr/bin/env python

import sys

for line in sys.stdin:

    data = line.strip().split("\t")

    if len(data) != 6:
        raise ValueError("Expected 6 elements, got {0}: {1}".format(len(data), line))

    date, time, item, category, sales, payment = data

    if category in ["Computers", "Cameras", "Video Games"]:
        sys.stdout.write("{0}\t{1}\n".format(category, sales))
