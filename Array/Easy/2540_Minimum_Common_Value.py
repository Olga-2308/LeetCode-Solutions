class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        # We create a set from one array so that the search is carried out instantly
        num = set(nums1)

        # Using a loop, we check the values ​​from the second array. 
        # Since the arrays are sorted, the first number that is found in both arrays is the answer.
        for n in nums2:
            if n in num:
                return n

        # If no common number is found, then we return -1
        return -1