class Solution:
    def findGCD(self, nums: List[int]) -> int:

        # find the minimum and maximum values ​​from the list, as required in the problem statement
        min_num = min(nums)
        max_num = max(nums)

        # find the greatest common divisor
        divisor = gcd(min_num, max_num)

        return divisor