class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        # The problem statement states that to achieve the result, you can only subtract one unit at a time. 
        # In this case, you need to figure out how many units need to be subtracted. 
        # To do this, you need to find the remainder of the sum of the numbers, 
        # which must be subtracted in order to obtain a number that is divisible by k without a remainder.

        # find the sum of numbers in an array
        total = sum(nums)

        # find the remainder after dividing by k
        count = total % k

        return count