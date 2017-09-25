#!/bin/python

import sys
one_count = 0
max_one_count = 0
n = int(raw_input().strip())

while n is not 0:
    remainder = n % 2
    n = n / 2
    if remainder is 1:
        one_count += 1
        max_one_count = max(one_count, max_one_count)
    else:
        one_count = 0
print max_one_count