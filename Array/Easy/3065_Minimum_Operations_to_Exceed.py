class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        # create a counter to count the number of numbers that are less than a given number.
        counter = 0

        # create a loop in which we work with each number in the list
        for num in nums:

            # If the number is less than the specified number, then we increase the counter by 1
            if num < k:
                counter += 1

        return counter