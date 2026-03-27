class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # sort the list where the numbers are in ascending order
        nums.sort()

        # take the last two numbers under the indices -1 and -2 respectively and perform calculations using the formula
        result = (nums[-1] - 1) * (nums[-2] - 1)

        return result
    

#       nums.sort()
#       rev_nums = nums[::-1] (expand the list so that the first two maximal elements are in the first places)
#       for i in range(0, 1): (create a loop in which we perform one iteration)
#           result = (rev_nums[i] - 1) * (rev_nums[i+1] - 1)
#   return result