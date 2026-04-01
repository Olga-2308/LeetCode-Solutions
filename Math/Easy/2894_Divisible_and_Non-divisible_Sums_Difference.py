class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        # create variables for numbers
        num1 = 0
        num2 = 0

        # create a loop in which we iterate over the numbers in order from 1 to n inclusive
        for i in range(1, n+1):

            # If the index of a number is not divisible by m without a remainder, then add the index to the first list
            if i % m != 0:
                num1 += i
            
            # otherwise we add the index of the number to the second list
            else:
                num2 += i

        # find the difference between variables
        result = num1 - num2

        return result