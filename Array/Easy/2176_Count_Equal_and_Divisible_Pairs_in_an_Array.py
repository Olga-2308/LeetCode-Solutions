class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        # create a counter to count pairs of numbers that match the problem statement.
        counter = 0

        # create a nested loop in which we work with pairs of numbers.
        for i in range(len(nums)):

            # ''' To avoid the number from interacting with itself in the iterations, we shift the start by 1
            # In this case, the loop will go through all pairs of adjacent numbers. '''
            for j in range(i+1, len(nums)):
                
                # ''' We check a pair of numbers to see if they meet the conditions, 
                # and if they do, we increase the counter by 1. '''
                if nums[i] == nums[j] and (i * j) % k == 0:
                    counter += 1

        return counter