class Solution:
    def sumAndMultiply(self, n: int) -> int:

        x = ""
        summa = 0

        #  We are looking for numbers in a string that are not equal to 0.
        for char in str(n):

            # As soon as a non-zero digit is found, we add the symbol to the string, 
            # and in the second variable we find the sum of all the digits
            if char != "0":
                x += char
                summa += int(char)

        # If a string does not contain a single digit other than zero, 
        # then the string is equal to the character 0
        if len(x) < 1:
            x = "0"

        # we return the product of variables as specified in the problem statement
        return int(x) * summa