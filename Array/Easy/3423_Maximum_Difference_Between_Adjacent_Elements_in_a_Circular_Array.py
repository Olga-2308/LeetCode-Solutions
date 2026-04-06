class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        # create a variable to find the maximum value
        maximum = 0

        # We create a loop in which we work with each number. 
        # Since we use the next number after the current one in each iteration, 
        # we shift the length by 1 to the left to avoid exceeding the loop limit.
        for i in range(len(nums)-1):

            # If the absolute value of the difference between two numbers exceeds the maximum, 
            # the variable is assigned a new maximum value
            if abs(nums[i] - nums[i+1]) > maximum:
                maximum = abs(nums[i] - nums[i+1])

        # The problem statement states that we are given a circular array, 
        # so we need to know the absolute value of the difference between the first and last elements of the list. 
        # Since the loop goes from start to finish, we'll check the last pair of numbers separately in the statement. 
        # If the absolute value of the difference is greater than the current maximum, we update the variable.
        if abs(nums[-1] - nums[0]) > maximum:
            maximum = abs(nums[-1] - nums[0])

        return maximum