class Solution:
    def arraySign(self, nums: List[int]) -> int:

        # create a variable to count the product of numbers in the array. 
        # We set the value to 1 so that the product does not equal 0.
        product = 1

        # create a loop in which we find the product of numbers
        for num in nums:
            product *= num

        # Next we return the values ​​according to the conditions of the problem
        if product == 0:
            return 0
        elif product > 0:
            return 1
        else:
            return -1
        
# It's also possible to write code that doesn't require multiplication. 
# You only need to know the final sign of the product.
# If there is 0 in the array, then the product of the numbers is always 0
# It is necessary to count the number of negative numbers. 
# If the number is even, then the product will be positive; 
# if it is odd, then it will be negative.

#   negative = 0 
#   for num in nums:
#       if num == 0:
#           return 0
#       if num < 0:
#           negative += 1
 
#       if negative % 2 == 0:
#           return 1
#       else:
#           return -1