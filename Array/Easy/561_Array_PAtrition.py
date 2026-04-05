class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        # To find the maximum sum of numbers formed from the minimum values ​​of each pair, 
        # it is necessary to distribute these numbers evenly over the entire length of the list. 
        # This way, large numbers will not be crowded out by small ones.

        # sort the list to evenly distribute the smallest numbers in pairs
        nums.sort()

        # create a variable in which we will find the sum of numbers
        result = 0

        # Since the list is sorted, the minimum number in the pair is in first place. 
        # Therefore, it is necessary to create a loop with a step of 2, 
        # in which each minimum number from the pairs will be taken.
        for i in range(0, len(nums), 2):

            # add each minimum number to the common variable
            result += nums[i]

        return result