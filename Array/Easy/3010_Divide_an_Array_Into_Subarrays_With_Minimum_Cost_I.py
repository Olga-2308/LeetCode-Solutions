class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        '''
        To find the minimum sum of the first elements of each subarray, 
        we must determine the minimum values ​​in the original array. 
        These points will be the starting points of each of the three arrays.
        '''

        # We create three variables that will contain the minimum values ​​of the array. 
        # The first element will always be the minimum possible start of the first subarray. 
        # We need to find the second and third start. 
        # To do this, we find the minimum value each time and, 
        # before writing it to the second position, move the current second position to the third.
        first = nums[0]
        second = float('inf')
        third = float('inf')

        for i in range(1, len(nums)):
            if nums[i] < second:
                third = second
                second = nums[i]
            elif nums[i] < third:
                third = nums[i]

        return first + second + third