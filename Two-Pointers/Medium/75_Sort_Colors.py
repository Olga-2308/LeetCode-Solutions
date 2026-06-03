class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        Since the array only contains three digits, three pointers can be used for sorting. 
        The first pointer collects 0, the second pointer collects 2 from the right, 
        and the third pointer rearranges the digits.
        '''
        
        # We determine the positions of all the pointers. 
        # We will sort the numbers from left to right.
        i = 0
        k = 0
        j = len(nums) - 1

        # The loop continues until the second pointer meets the third (right) pointer. 
        # This means all the numbers in the array are sorted.
        while k <= j:

            # If the number under the center pointer is 0, it needs to be moved to the left. 
            # We swap the pointer values ​​and move each pointer one step to the right.
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1

            # If the number under the central pointer is 2, then this number must be on the right side of the array, 
            # so we swap the values ​​of the numbers under the pointers and move the right pointer one step to the left.
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1

            # If the number under the central pointer is 1, then we cannot move it anywhere, 
            # since it must remain in the center, and we simply move the central pointer one step to the right.
            else:
                k += 1