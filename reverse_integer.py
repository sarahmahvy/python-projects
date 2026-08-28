#!usr/bin/env python3

def reverse(x:int):
    num = str(x)
    reverse = num[::-1]
    if reverse[-1] == "-":
        reverse = reverse[:-1]
        if int(reverse) > (2**31 - 1) or int(reverse) < (-2**31):
                return 0
        else:
            output = "-{}".format(reverse)
    elif int(reverse) > (2**31 - 1) or int(reverse) < (-2**31):
        return 0
    else:
        output = "{}".format(reverse)
    return int(output)

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))
print(reverse(1534236469))