class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # There are several possible locations for a given number. 
        # It is necessary to consider all the options in order.

        # If the given number is less than all the numbers in the array, 
        # (less than the minimum number in the sorted array) then we return 0. 
        # Since the number will be the smallest in the array, it will take the first place under index 0
        if target < nums[0]:
            return 0
        
        # If the given number is greater than the maximum in the array, it will occupy the last position in the array. 
        # To determine the index of this position, you need to find the array length, 
        # which will show the index of the next number (the index starts at 0, and the number of numbers starts at 1,
        # so the position of the last number is the index number for the next one).
        elif target > nums[-1]:
            return len(nums)
        
        # If the given number is in the array, then we use a loop to find this number and return its index
        elif target in nums:
            return nums.index(target)

        # If a number is within the range of the given array, we need to determine its position in the list. 
        # To do this, we create a loop in which we check pairs of numbers. 
        # If a number is within the range of two adjacent numbers, 
        # it will be placed in the next position after the current one in the loop. 
        # Therefore, we return the index of the current number incremented by one (the next position).
        for i in range(len(nums)):
            if nums[i] < target < nums[i+1]:
                return i + 1