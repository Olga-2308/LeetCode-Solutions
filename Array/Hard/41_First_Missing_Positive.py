class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        '''
        We convert the array into a set to avoid checking for duplicates. 
        We check all values ​​from 1 to the length of the original array, 
        since the array cannot contain values ​​greater than its length. 
        If no such values ​​are found, we return the first positive value outside the array's bounds, 
        which is guaranteed to be the minimum required value.
        '''

        numbers = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in numbers:
                return i

        return len(nums) + 1

        '''
        You can also search for the maximum and minimum values. 
        If the minimum is greater than 1, then we return 1. 
        The maximum value is the boundary of the cycle, 
        in which all numbers are checked in order (redundantly).

        min_num = float('inf')
        max_num = 0
        numbers = set(nums)

        for num in numbers:
            if num <= 0:
                continue
            else:
                min_num = min(min_num, num)
                max_num = max(max_num, num)

        if min_num > 1:
            return 1

        for i in range(min_num, max_num): # range(min_num, len(nums) + 1)
            if i not in numbers:
                return i
        else:
            return max_num + 1
        '''