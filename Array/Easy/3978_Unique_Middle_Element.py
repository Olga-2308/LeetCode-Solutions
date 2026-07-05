class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:

        # We find the index of the central number in the array. 
        # Since the array length is odd, integer division by will yield the midpoint 
        # (taking into account indexing starting with 0).
        indx = len(nums) // 2
        counter = 0

        # using a loop we count the number of occurrences of a given number in the array
        for i in range(len(nums)):
            if nums[i] == nums[indx]:
                counter += 1

        return counter == 1