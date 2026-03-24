class Solution:
    def alternateDigitSum(self, n: int) -> int:

        # create a variable in which we will write the sum
        result = 0

        # convert the number into a string so we can work with each character separately
        s = str(n)

        # we create a loop in which we iterate over each character of the string (index 0 - character 1)
        for i in range(len(s)):
            # we take a character from a string and turn it into a number
            digit = int(s[i])

            # ''' if the index of a number is even (or 0), then the number is added 
            # (if the index meets the condition, then we write the number that is under this index into the result) '''
            if i % 2 == 0:
                result += digit
            # otherwise the number is subtracted
            else:
                result -= digit
        
        return result