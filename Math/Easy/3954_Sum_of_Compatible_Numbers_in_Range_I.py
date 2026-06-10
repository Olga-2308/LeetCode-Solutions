class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:

        total = 0

        # To determine the beginning of a cycle, we need to find the difference abs(n - x) <= k.
        #  Since we are looking for a positive number and determining the difference without the absolute value, 
        # we need to specify two values ​​and choose the maximum if the difference between the numbers is negative.
        start = max(1, n - k)

        # find the end of the cycle
        end = n + k

        # We select a number within the given loop limits. 
        # If at the current iteration the number meets all the conditions of the problem, 
        # then we immediately return it.
        for x in range(start, end + 1):
            if abs(n - x) <= k and (n & x) == 0:
                total += x

        return total
