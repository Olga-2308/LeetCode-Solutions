class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        '''
        Since a balancing string can be formed from any sequence, 
        this means that each pair of symbols is considered balanced and can be removed. 
        The remaining symbols are those that lack a pair to create balance.
        '''

        a = 0
        b = 0

        # we count the number of each character in the line
        for char in s:
            if char == "a":
                a += 1
            else:
                b += 1

        # we return the number of identical characters that remain unpaired
        return abs(a - b)