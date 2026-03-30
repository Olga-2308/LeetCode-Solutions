class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        # create a counter to count the number of matching pairs.
        counter = 0

        # create a nested loop in which we iterate over pairs of numbers
        for i in range(len(nums)):

            # To avoid checking repeating pairs of numbers and the number itself, we move the step by i+1
            for j in range(i+1, len(nums)):

                # If the absolute value of the difference between the numbers is equal to K, then we increase the counter by one.
                if abs(nums[i] - nums[j]) == k:
                    counter += 1

        return counter