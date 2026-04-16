class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        '''
        Since the strings differ from each other by only one character, 
        we can find the sum of all the codes for each character. 
        And after finding the difference, the difference is the code for the extra character.

        Create variables to calculate the sum of each row
        '''
        sum_s = 0
        sum_t = 0

        '''
        create cycles in which we add the code of each symbol in turn.
        '''
        for char in s:
            sum_s += ord(char)

        for char in t:
            sum_t += ord(char)

        '''
        find the difference between the sums and return the symbol that is under the resulting value.
        '''
        alpha = chr(sum_t - sum_s)

        return alpha