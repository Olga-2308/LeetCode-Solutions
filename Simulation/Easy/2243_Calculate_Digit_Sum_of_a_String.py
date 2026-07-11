class Solution:
    def digitSum(self, s: str, k: int) -> str:

        #  the loop runs until the string length is greater than the specified length
        while len(s) > k:

            # we create a variable into which we will add the result of the sum of the digits of each part of the string
            current = ""
            
            # we create a loop that alternately steps through a step equal to a given length
            for i in range(0, len(s), k):

                # we determine a cut equal to a given length
                part = s[i:i+k]

                # using a loop we calculate the sum of the digits of the slice
                digit = 0
                for char in part:
                    digit += int(char)

                # add the result to the current line
                current += str(digit)
            
            # After the current loop is complete, we update the main line and start 
            # a new loop with a new string of characters.
            s = current

        return s
