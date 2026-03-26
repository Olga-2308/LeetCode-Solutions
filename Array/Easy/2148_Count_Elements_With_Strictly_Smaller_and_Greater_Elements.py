class Solution:
    def countElements(self, nums: List[int]) -> int:

        counter = 0

        # find the maximum and minimum numbers in the list
        max_num = max(nums)
        min_num = min(nums)

        # ''' create a loop in which we check each element for compliance with the double inequality; 
        # if the number matches, we increase the counter by 1. '''
        for i in range(len(nums)):
            if min_num < nums[i] < max_num:
                counter += 1

        return counter