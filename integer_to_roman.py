def inttoroman(num:int):
    roman = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
    result = ""
    while num != 0:
        for key in sorted(roman.keys(), key=lambda x: roman[x], reverse=True):
            if num >= roman[key]:
                result += key
                num -= roman[key]
                break
    return result

response = True
while response:
    num = int(input("Enter a number you want to convert to Roman numeral: "))
    if num <= 0:
        print("Please enter a valid positive integer. (press enter to continue)")
        continue
    print(inttoroman(num))
    response = input("Do you want to continue? (y/n): ")
    if response.lower() == 'n':
        response = False