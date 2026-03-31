class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

#The problem requires finding the maximum difference between two products. 
# To obtain the maximum result, subtract the product of the minimum numbers from the product of the maximum numbers. 
# In this case, the difference will be the largest of all possible.

        # sort the list to determine the indices of the extreme numbers
        nums.sort()

        # find the difference between the product of two maximum numbers and two minimum numbers
        result = (nums[-1] * nums[-2]) - (nums[0] * nums[1])

        return result