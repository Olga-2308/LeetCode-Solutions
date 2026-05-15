class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        It is necessary to find the minimum value of the array
        '''

        # we define the boundaries of the array
        left = 0
        right = len(nums) - 1

        # We will search for the minimum value using binary search, 
        # the loop runs until the left boundary is less than the right one
        while left < right:

            # find the central index of the current array
            mid = left + (right - left) // 2

            # If the number in the center of the array is greater than the number on the right, 
            # this means that there cannot be a minimum number on the left side, 
            # and we remove all the numbers from the left side to the center and update the array
            if nums[mid] > nums[right]:
                left = mid + 1

            # If the central number is smaller than its neighbor to the right, 
            # this means that there are even smaller numbers on the left and we don't need the right part of the array 
            # (the central number may be a minimum, so we leave it in the new array)
            else:
                right = mid

        return nums[left]