#!/usr/bin/env python3
def isUgly(n:int) -> bool:
    if n != 0 and(n%2 == 0 or n%3 == 0 or n%5 == 0):
        while n%2 == 0:
            n = n//2
        while n%3 == 0:
            n = n//3
        while n%5 == 0:
            n = n//5
        if n == 1:
            return True
        else:
            return False
    elif n == 1:
        return True
    else:
        return False

print(isUgly(6))   
print(isUgly(1))
print(isUgly(14)) #should return false
print(isUgly(0))

