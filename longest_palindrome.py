#This code takes longer than the code in the "def longestPalindrome.py" file.
def longestPalindrome(s: str):
        s = s.replace(" ", "")
        s = s.lower()
        palindrome=""
        start = 0
        for j in range(len(s)):
            loop = s
            start += 1
            for i in range(len(loop)):
                temp = s[i:start]
                if temp == ''.join(reversed(temp)) and len(palindrome) < len(temp):
                
                    palindrome = temp
                else:
                    continue
            continue            
        return palindrome

response = True
while response:
    s = input("Enter a string to find the longest palindrome: ")
    if s == "":
        print("Please enter a valid string. (press enter to continue)")
        continue
    print(longestPalindrome(s))
    response = input("Do you want to continue? (y/n): ")
    if response.lower() == 'n':
        response = False
