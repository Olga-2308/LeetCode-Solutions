class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        # create a counter to count pairs of numbers that match the conditions of the problem.
        counter = 0

        # create a nested number system for working with pairs of numbers.
        for i in range(len(nums)):

            # in the second loop we shift the index by 1 so that a pair of different numbers is considered
            for j in range(i+1, len(nums)):

                # If two numbers fulfill the conditions of the problem, the counter increases by 1
                if i < j and nums[i] == nums[j]:
                    counter += 1

        return counter