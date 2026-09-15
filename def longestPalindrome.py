def longestPalindrome(s:str):
    palindrome = ""
    palindromelen  = 0
    for i in range(len(s)):
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > palindromelen:
                palindrome = s[l:r+1]
                palindromelen = r-l + 1
            l -= 1
            r += 1

        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > palindromelen:
                palindrome = s[l:r+1]
                palindromelen = r - l + 1
            l -= 1
            r += 1

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