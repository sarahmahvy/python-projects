def isPalindrome(x: int) -> bool:
        palindrome = str(x)
        if palindrome == ''.join(reversed(palindrome)):
            return "true"
        else:
            return "false"

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(-101))