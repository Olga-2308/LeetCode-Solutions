class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        '''
        We can split the original array into two different arrays with virtually no stringent restrictions. 
        This means we need to find a break in the array (a pair of numbers) whose difference is minimal. 
        The minimal difference is possible by searching for paired numbers in sorted order. 
        When splitting the array into two parts, one element of the pair will be the minimum in its array, 
        and the second element of the pair will be the maximum in the second array.
        '''

        # We sort the array to easily find the minimum difference between numbers.
        nums.sort()

        current = 0

        # we set the maximum value of the variable so 
        # that the first result found is guaranteed to be less than the current infinity
        result = float('inf')

        # We check each pair of numbers in the array, so we shift the end of the loop by -1
        for i in range(len(nums) - 1):

            # we find the current difference of numbers
            current = nums[i+1] - nums[i]

            # we determine the minimum value
            if current < result:
                result = current

        return result