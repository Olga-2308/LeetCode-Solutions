class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

# The problem statement states that in order to return true, 
# the list of numbers must have the following form: (even)-odd-even-odd, etc. 

# This means that if a pair of numbers is even-even or odd-odd, then false is immediately returned. 
# It is worth noting that: 
    # even + even = even 
    # even + odd = odd 
    # odd + odd = even 
# From these equalities it follows that in our problem, 
# if two adjacent numbers add up to an odd number, then the list returns true. 

# And if the sum of the numbers is even, 
# then this means that two adjacent numbers in the list are even-even or odd-odd, which returns false.

        # First, we check if there are lists with one element. If there are, we return true.
        if len(nums) < 2:
                return True

        # We create a loop in which we check each pair of numbers in the list, 
        # where the pair of numbers is the current number and its neighboring number to the right. 

        # We set the loop boundary and subtract one from the length to avoid exceeding the bounds. 
        # In the final iteration, the loop reaches the penultimate number and takes its neighboring number—the last one.
        for i in range(len(nums)-1):

            # If the sum of two adjacent numbers is even, then return false
            if (nums[i] + nums[i+1]) % 2 == 0:
                return False

        # otherwise, after a complete check of all pairs of numbers in the list, we return true
        else:
            return True