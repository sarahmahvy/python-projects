#!usr/bin/env python3

def smallestRepunitDivByK(k:int) -> int:
    if k%2 == 0 or k%5 == 0:
        return -1
    remainder = 1
    length = 1
    if k == 1:
        return 1
    while remainder != 0:
        remainder = ((remainder * 10) + 1) % k
        length += 1
    return length

print(smallestRepunitDivByK(1))
print(smallestRepunitDivByK(2))
print(smallestRepunitDivByK(3))