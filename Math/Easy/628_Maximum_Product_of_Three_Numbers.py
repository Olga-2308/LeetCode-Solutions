class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        # To find the maximum numbers in an array, you need to sort it, 
        # and then the maximum values ​​will be at the end of the array.
        nums.sort()

        # Since the array may contain negative values, the modulus of which may be significantly greater than positive numbers, 
        # there are two options for finding the maximum product of three numbers

        # In the first case, we find the maximum product of the three largest numbers in the sorted array
        result1 = nums[-1] * nums[-2] * nums[-3]

        # If among the negative numbers there is a number whose absolute value is greater than the maximum number among the positive numbers, 
        # then only two negative numbers can be multiplied to obtain a positive number and multiplied by one maximum positive number
        result2 = nums[0] * nums[1] * nums[-1]

        # as a result we return the maximum value
        return max(result1, result2)