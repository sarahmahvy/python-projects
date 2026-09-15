#!/usr/bin/env python3

def canMakeArithmeticProgression(arr:List[int]) -> bool:
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True

response = True
while response:
    arr = list(map(int, input("Enter the list of numbers separated by a space: ").split()))
    if arr == [] or len(arr) < 2:
        print("Please enter a valid list of numbers. (press enter to continue)")
        continue
    print(canMakeArithmeticProgression(arr))
    response = input("Do you want to continue? (y/n): ")
    if response.lower() == 'n':
        response = False