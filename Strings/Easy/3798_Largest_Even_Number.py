class Solution:
    def largestEven(self, s: str) -> str:
        '''
        To get the largest even number, you need to remove numbers from the least significant digits. 
        If the last digit is even, then the number is even; if it's odd, then remove the outer digits until you end up with 2.
        '''
        
        # We create a loop in which we check each digit from the end
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "2":

                # As soon as we encounter an even digit, we return the slice from the beginning up to and including this digit.
                return s[:i+1]
        
        # If there are no even digits, then we return an empty string.
        return ""