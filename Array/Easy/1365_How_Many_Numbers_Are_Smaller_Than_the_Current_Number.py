class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # create an empty list to record the results
        result = []

        # ''' sort the original list in ascending order 
        # (this way we can calculate how many elements are less than a specific number 
        # - these numbers will be sorted and placed to the left of the specific number) '''
        sort_nums = sorted(nums)

        # create a loop in which we work with each element in order
        for num in nums:

            # ''' looking for the index of a number in a sorted list; 
            # the index in a sorted list shows the number of numbers that are less than the one being checked. '''
            indx = sort_nums.index(num)
            result.append(indx)

        return result