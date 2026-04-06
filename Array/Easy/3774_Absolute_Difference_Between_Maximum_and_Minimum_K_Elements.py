class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:

        # sort the list to easily determine the maximum and minimum values ​​in the array.
        nums.sort()

        # We find the sum of the maximum elements. 
        # The maximum numbers in a sorted list are at the end of the row, 
        # so we need to specify the slice in which we access the negative indices. 
        # (k = 2, [-k:] --> -2, -1 - two elements)
        largest = sum(nums[-k:])

        # We find the sum of the minimum elements that are at the beginning of the list. 
        # Therefore, we take a slice from the beginning to K.
        smallest = sum(nums[:k])

        # return the absolute value of the difference between the maximum and minimum amounts
        return abs(largest - smallest)