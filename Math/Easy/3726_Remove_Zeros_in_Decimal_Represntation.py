class Solution:
    def removeZeros(self, n: int) -> int:

        # create an empty string for numbers
        result = ''

        # We create a loop in which we check each character. 
        # Since we are given a number in which we need to check each digit, we turn the number into a string.
        for char in str(n):

            # If the digit is not 0, then we add it to a new line
            if char != '0':
                result += char

        # we return the obtained result as a number
        return int(result)  