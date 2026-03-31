class Solution:
    def minMoves(self, nums: List[int]) -> int:

        # The problem statement makes it clear, 
        # that we need to determine the minimum number of steps required to make all numbers in the list equal. 
        # Since we can increment a number by 1 in a single step, 
        # it's clear that we need to align all numbers with the largest number in the list.

        # create a variable that will contain the total number of steps
        total = 0

        # find the maximum number
        max_num = max(nums)

        # create a loop in which we work with each number
        for i in range(len(nums)):

            # If the number from the loop is equal to the maximum number, 
            # then it is the maximum number itself, and there is no need to increase it, otherwise:
            if nums[i] != max_num:

                # find the number of steps (the difference in numbers) that is necessary to equate the number with the maximum
                moves = max_num - nums[i]

                # add the number of steps to the total result
                total += moves

        return total