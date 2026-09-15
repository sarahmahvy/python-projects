#!usr/bin/env python3

def selfDividingNumbers(left:int, right:int) -> List[int]:
    result = []
    for digit in range(left, right+1):
        if '0' not in str(digit):
            if digit < 10:
                result.append(digit)
            else:
                temp = str(digit)
                for i in temp:
                    if int(temp) % int(i) != 0:
                        divisible = False
                        break
                    else:
                        divisible = True
                if int(temp) not in result and divisible:
                    result.append(digit)
    return result

response = True

while response:
    left = int(input("Enter the start number: "))
    right = int(input("Enter the ending number: "))
    print(selfDividingNumbers(left, right))
    response = input("Do you want to continue? (y/n): ")
    if response.lower() == 'n':
        response = False