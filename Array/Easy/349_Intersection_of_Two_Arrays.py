class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Since we need to find the intersection of numbers in both arrays, it is enough to check only one of them.

        # create an empty list where we will add unique intersections of numbers
        result = []

        # create a loop in which we check the numbers from the first list.
        for num in nums1:

            # If a number is in the second list, then it is an intersection
            # At the same time, you need to check whether the same number is already in the final list. 
            # This is necessary to ensure that the result contains only unique numbers. In this case, duplicates are not added.
            if num in nums2 and num not in result:
                result.append(num)

        return result