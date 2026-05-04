class Solution:
    def minimumLength(self, s: str) -> int:
        '''
        To determine the minimum length of a new string, we need to know how many characters we can remove. 
        The problem statement states that if a character appears three or more times in a string, 
        it means that a pair can be removed (left - remove, center - remain, right - remove). 
        If there are more than three characters, the deletion scheme is as follows: 5 - 2 - 2 = 1. 
        One character will always remain in the string, and if there are two or fewer characters, 
        they will also remain in the string, since there is no valid triplet that would allow the outermost characters to be removed.
        '''

        d = {}
        counter = 0

        # We create a dictionary that records the frequency of each character in the string.
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        # in a loop we check the frequency of each character in the string
        for char, freq in d.items():

            # If the frequency is less than three, then deletion is impossible, 
            # and the value is added to the final length
            if freq < 3 and freq > 0:
                counter += freq

            # If the frequency is greater than 3, then it is necessary to determine 
            # how many pairs of characters can be removed
            else:

                # To do this, we subtract 2 (symbols) from the frequency each time, as long as this is possible. 
                # And this is possible as long as there are three identical symbols.
                while freq >= 3:
                    freq -= 2

                # as soon as the frequency becomes less than three, 
                # deletion is impossible and we add the remainder to the length of the string
                counter += freq

        return counter