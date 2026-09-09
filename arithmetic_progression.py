#!/usr/bin/env python3

def canMakeArithmeticProgression(arr:List[int]) -> bool:
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True

print(canMakeArithmeticProgression([3,5,1]))
print(canMakeArithmeticProgression([1,2,4]))
print(canMakeArithmeticProgression([1,3,5,7]))
print(canMakeArithmeticProgression([1,2,3,4,5]))
print(canMakeArithmeticProgression([1,2,3,5,7]))