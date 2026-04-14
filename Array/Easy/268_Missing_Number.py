class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # find the length of the array to determine the sum of all elements
        l = len(nums)

        # Since the problem is a sequence of numbers from 1 to n, except for one missing number, 
        # it is necessary to calculate the sum of the complete sequence using the following formula.
        all_sum = l * (l + 1) // 2

        # then we find the sum of the current array of numbers
        current_sum = sum(nums)

        # To find the missing number, you need to subtract the current sum from the total sum of the array of numbers
        result = all_sum - current_sum

        return result