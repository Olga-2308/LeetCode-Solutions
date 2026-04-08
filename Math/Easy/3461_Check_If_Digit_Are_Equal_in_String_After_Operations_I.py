class Solution:
    def hasSameDigits(self, s: str) -> bool:

        # To make sure that only two characters remain in the new line, 
        # you need to shorten the line until its length becomes 2
        while len(s) != 2:

            # We create a new empty string to store the newly received characters. 
            # This is necessary so that during the loop, the original string changes only after all the digits have changed, 
            # and not after each new number is found.
            new_s = ''

            # We create a loop in which we find new digits in the string. 
            # Since each iteration works with a pair of numbers, 
            # we reduce the step boundary by 1 so as not to go beyond the limit.
            for i in range(len(s)-1):

                # We find a new number according to the problem statement. 
                # Since the number is a string in its original form, 
                # when performing arithmetic operations, the symbol is converted into a number.
                num = (int(s[i]) + int(s[i+1])) % 10

                #  We convert the resulting number into a string and add it to a new variable.
                new_s += str(num)
            
            # We assign the original variable a new value, which we obtained after searching for all the new numbers.
            # The string is shortened, and the outer loop continues to run until there are two characters left in the string.
            s = new_s

        # If the two remaining characters are equal, then return true, otherwise return false.
        return s[0] == s[-1]