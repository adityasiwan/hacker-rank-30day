#!/bin/python

import sys

n = int(raw_input().strip())
for i in range(1, 21):
    print "%s x %s = %s" % (n, i, n*i)
