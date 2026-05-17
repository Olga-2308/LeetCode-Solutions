class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        from math import floor

        # we find the average value using the formula
        target = sum(nums) / len(nums)

        # round the number to the nearest whole number
        n = floor(target)

        # We transform the array itself into a set, since we need to find a pair of different numbers
        numbers = set(nums)

        # Since the average value is rounded down, you need to add 1 to find a number that is strictly greater than the average value.
        result = n + 1

        # If the average value is negative, then the corresponding number can also be negative, 
        # but according to the problem statement, it is necessary to return a number equal to or greater than 1. 
        # Therefore, we return 1 if we received the average value as a negative number.
        result = max(1, n + 1)

        # We start a loop in which we look for the first number that is not in the array. 
        # If the current value is present, we add 1 and check the next one.
        while result in numbers:
            result += 1

        return result