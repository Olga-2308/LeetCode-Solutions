class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        # create variables in which we will count the number of positive and negative numbers
        count_pos = 0
        count_neg = 0

        # create a loop in which we check each number
        for num in nums:

            # If the number is less than 0, we increase the negative number counter.
            if num < 0:
                count_neg += 1

            # If the number is greater than 0, then we increase the counter of positive numbers
            elif num > 0:
                count_pos += 1

        # Since 0 does not fall into any of the categories, it is not included in the test conditions

        # find the maximum number among positive and negative numbers and return the result.
        result = max(count_pos, count_neg)

        return result