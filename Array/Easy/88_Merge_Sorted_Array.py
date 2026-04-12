class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # In the original array, we take a slice from m to the end where 0 is located, 
        # and replace them with numbers from the second array
        nums1[m:] = nums2

        # sort the resulting list as required in the problem statement
        nums1.sort()