class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # create a counter to count matching pairs.
        counter = 0

        # create a nested loop in which we work with each number
        for i in range(len(nums1)):

            # since lists can have different numbers of elements, 
            # it is necessary to take this length into account within the loop boundaries
            for j in range(len(nums2)):

                # If a pair of numbers corresponds to the condition of the problem, then we increase the counter by one
                if nums1[i] % (nums2[j] * k) == 0:
                    counter += 1

        return counter 