class Solution:
    def minChanges(self, s: str) -> int:
        '''
        To make all substrings beautiful with a minimum number of changes, 
        the string must be split into pairs, where each pair is a substring. 
        If the pair of characters is the same, the string is already beautiful and no changes are needed. 
        If the characters are different, then only one step is required to make the string beautiful.
        '''

        counter = 0

        # we create a loop in which we check pairs of numbers, so step 2
        for i in range(0, len(s) - 1, 2):

            # If the characters are different, then we increase the counter by 1, 
            # since one step is needed to make a nice line
            if s[i] != s[i+1]:
                counter += 1

        return counter