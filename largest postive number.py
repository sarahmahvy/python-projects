def findMaxK( nums: List[int]) -> int:
        large = 0
        for number in nums:
            if abs(number) > large:
                large = abs(number)
        return large

print(findMaxK([-1,10,6,7,-7,1]))
print(findMaxK([-10,8,6,7,-2,-3]))