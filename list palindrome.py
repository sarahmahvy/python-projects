def isPalindrome(head: Optional[ListNode]) -> bool:
        temp = ""
        for num in head:
             temp += str(num)
        
        if temp == temp[::-1]:
            return True
        else:
            return False

print(isPalindrome([1,2,2,1]))
print(isPalindrome([1,2]))