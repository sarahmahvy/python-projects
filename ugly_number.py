#!/usr/bin/env python3
def isUgly(n:int) -> bool:
    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        return True
    elif n == 1:
        return True
    else:
        return False

print(isUgly(6))   
print(isUgly(1))
print(isUgly(14)) #should return false

