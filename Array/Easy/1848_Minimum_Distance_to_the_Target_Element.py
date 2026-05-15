class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        min_diff = float('inf')
        diff = 0

        # using a loop we find the required number
        for i in range(len(nums)):
            if nums[i] == target:

                # We calculate the difference using the formula
                diff = abs(i - start)

                # we determine the minimum value
                if diff < min_diff:
                    min_diff = diff

        return min_diff