class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:

# The problem statement states that pairs of numbers from two lists become equal if the same number is added (subtracted) from each pair.
#  To find this common number, we need to sort both lists in ascending order, 
# which will yield pairs that can be equalized by a single number.

        # To find this number, you need to subtract the minimum number from the first list from the minimum value from the second list
        result = min(nums2) - min(nums1)

        return result
    

# nums1.sort()
# nums2.sort()
# result = nums2[0] - nums1[0]