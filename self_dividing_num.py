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
                    if int(temp) % int(i) == 0:
                        if int(temp) not in result:
                            result.append(digit)
                    else:
                        continue
    return result

print(selfDividingNumbers(1, 22))
print(selfDividingNumbers(47, 85))