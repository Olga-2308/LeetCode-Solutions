class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
        A triangle can be formed from sides if the sum of two of them is greater than the third side 
        and the difference between these sides is less than the third
        '''

        # sort the array in descending order to find the maximum perimeter
        nums.sort(reverse = True)

        # Checking a triple of numbers using a loop, we specify -2 to avoid going beyond the array's bounds
        for i in range(len(nums) - 2):

            # If the sum and difference of the sides meet the conditions for creating triangles, 
            # we return the sum of these sides (the perimeter of the triangle)
            if nums[i] + nums[i+1] > nums[i+2] and abs(nums[i] - nums[i+1]) < nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0