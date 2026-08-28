def shortestPalindrome(s:str):
    def is_pali(s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
            return True
    for r in reversed(range(len(s))):
            if is_pali(s, 0, r):
                result = s[r+1:][::-1] + s
                return result
            else:
                continue
    return ""


print(shortestPalindrome("aacecaaa"))
print(shortestPalindrome("abb"))
print(shortestPalindrome("abcd"))
print(shortestPalindrome("aabba"))