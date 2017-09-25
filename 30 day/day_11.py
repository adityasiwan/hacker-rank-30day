#!/bin/python

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

sum = 0
max_sum = -9 * 7

for x in range(0, 4):
    for y in range(0, 4):
        sum = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
        max_sum = max(sum, max_sum)
print max_sum
