class Solution:
    def sumOfMultiples(self, n: int) -> int:

        # we create a variable to calculate the sum
        result = 0

        # we create a loop from 1 to n+1 to check all numbers in a given range (n+1 to check the last number as well)
        for i in range(1, n+1):

            # we check whether one of the three listed conditions is met (or - one of)
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:

                # if the condition is met, we add the number to the variable
                result += i

        return result