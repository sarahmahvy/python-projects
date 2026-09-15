def isPalindrome(head: Optional[ListNode]) -> bool:
        temp = ""
        for num in head:
             temp += str(num)
        
        if temp == temp[::-1]:
            return True
        else:
            return False

response = True
while response:
    
        head = list(map(int, input("Enter the elements of the linked list separated by spaces to find if the list is a palindrome: ").strip().split()))
        if head == []:
            print("Please enter a valid list of numbers. (press enter to continue)")
            response = True
        print(isPalindrome(head))
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() == 'n':
            response = False