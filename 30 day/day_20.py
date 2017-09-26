#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
numberofSwaps = 0
for i in range(0, n):
    for j in range(0, n-1):
        if a[j] > a [j+1]:
            a[j] , a[j+1] = a[j+1], a[j]
            numberofSwaps += 1
    if numberofSwaps is 0:
        break
print "Array is sorted in %s swaps." %(numberofSwaps)
print "First Element: %s" %(a[0])
print "Last Element: %s" %(a[n-1])