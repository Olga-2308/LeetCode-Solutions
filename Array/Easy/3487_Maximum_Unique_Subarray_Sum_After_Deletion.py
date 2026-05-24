class Solution:
    def maxSum(self, nums: List[int]) -> int:

        total = 0

        # Using a set, we remove all duplicates so that the elements in the array become unique, 
        # as required by the problem statement.
        numbers = set(nums)

        # To get the maximum result, you need to add only positive numbers
        for num in numbers:
            if num > 0:
                total += num

        # If the result is greater than 0, then the array contains positive numbers 
        # and we immediately return the result
        if total > 0:
            return total

        # If the variable is 0, then the array contains only negative numbers, 
        # so we return the maximum of them.
        return max(numbers)  

        '''
        total = 0
        minimum = float('-inf')
        numbers = set(nums)

        for num in numbers:
            if num > 0:
                total += num
            elif num <= 0:
                minimum = max(minimum, num)

        if total > 0:
            return total
        else:
            return minimum 
        '''  