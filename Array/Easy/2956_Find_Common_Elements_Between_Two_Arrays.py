class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # create variables to count number matches
        answer1 = 0
        answer2 = 0

        # create a loop in which we check each number from the first list.
        for num in nums1:

            # If a number from the first list is in the second list, then we increase the counter by 1
            if num in nums2:
                answer1 += 1

        # create a loop in which we check each number from the second list.
        for num in nums2:

            # If a number from the second list is in the first list, then we increase the counter by 1
            if num in nums1:
                answer2 += 1

        # write down the result as indicated in the problem statement
        result = [answer1, answer2]

        return result