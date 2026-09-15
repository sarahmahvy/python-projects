def findMaxK( nums: List[int]) -> int:
        large = 0
        for number in nums:
            if abs(number) > large:
                large = abs(number)
        return large

response = True
while response:
    nums = list(map(int, input("Enter the list of numbers separated by a space to find the largest absolute value: ").split()))
    if nums == []:
        print("Please enter a valid list of numbers. (press enter to continue)")
        continue
    print(findMaxK(nums))
    response = input("Do you want to continue? (y/n): ")
    if response.lower() == 'n':
        response = False