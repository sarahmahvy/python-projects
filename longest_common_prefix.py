#!/usr/bin/env python3

def longestcommonprefix(strs:List[str]):
    prefix = ""
    strs = [s.lower() for s in strs]
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return prefix
        prefix += char
    return prefix

response = True
while response:
    strs = list(map(str, input("Enter the list of strings separated by a space to find the longest common prefix: ").split()))
    if strs == []:
        print("Please enter a valid list of strings. (press enter to continue)")
        continue
    if longestcommonprefix(strs) == "":
        print("There is no common prefix in the given list of strings.")
    else:
        print(longestcommonprefix(strs))
    response = input("Do you want to continue? (y/n): ")
    if response.lower() == 'n':
        response = False