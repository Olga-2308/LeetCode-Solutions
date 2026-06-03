class Solution:
    def reverse(self, x: int) -> int:

        # If the number is positive, then we convert it to a string to reverse the characters
        if x >= 0:
            num = str(x)[::-1]
            number = int(num)

        # If the number is negative, we temporarily make it positive by multiplying it by -1. 
        # Then we convert it to a string in the same way and reverse it. 
        # Then we multiply the number by -1 to make it negative again.
        else:
            xx = x * (-1)
            num = str(xx)[::-1]
            n = int(num)
            number = n * (-1)

        # We check the constraints and return the corresponding result.
        if number <= (-2 ** 31) or number >= (2 ** 31 -1):
            return 0
        else:
            return number