
import sys
def factorial(n):
    if(n is 0):
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = int(raw_input().strip())
    result = factorial(n)
    print result