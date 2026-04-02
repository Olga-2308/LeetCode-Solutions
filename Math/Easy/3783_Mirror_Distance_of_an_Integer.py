class Solution:
    def mirrorDistance(self, n: int) -> int:

        # We create a new variable in which we need to reverse the number. 
        # Since it's impossible to reverse the characters with integer variables, we need to convert the number to a string.
        new_n = str(n)[::-1]

        #  We find the absolute value of the difference between two mirror numbers. 
        # To perform the arithmetic operation, we need to convert the reversed string back into a number.
        result = abs(n - int(new_n))

        return result