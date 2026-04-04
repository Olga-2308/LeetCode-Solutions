class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        # To get an odd number in the binary system, it is necessary that the last digit of the number is always 1. 
    
        # And to get the maximum number, it is necessary that all 1's, except the last one, 
        # are in the most significant digits of the number.

        # find the number of 0 and 1 in a string
        zeroes = s.count('0')
        ones = s.count('1')

        # We connect the characters into a new line so that there is one 1 at the end, 
        # and all the others are at the beginning of the line, with all the 0s between the 1s
        result = '1' * (ones-1) + '0' * zeroes + '1'

        return result