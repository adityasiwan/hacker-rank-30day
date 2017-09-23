#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
rarr = map(str, arr[::-1])
print(" ".join(rarr))
