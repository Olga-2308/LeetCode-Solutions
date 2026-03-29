class Solution:
    def alternatingSum(self, nums: List[int]) -> int:

        # create a counter to calculate the amount
        result = 0

        # create a loop in which we work with each number in order
        for i in range(len(nums)):

            # If the index of a number is odd, then we subtract this number from the total result
            if i % 2 != 0:
                result -= nums[i]
            
            # If the index is even, then we add this number to the total result
            else:
                result += nums[i]

        return result