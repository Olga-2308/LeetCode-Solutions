class Solution:
    def maxDistinct(self, s: str) -> int:

        '''
        The condition specifies that a substring can only begin with a letter that hasn't previously been used to create a substring. 
        This means that each unique letter in the string produces one substring, and all duplicate letters are ignored. 
        To determine the number of unique letters without duplicates, you can turn the string into a set and return the length of that set. 
        Since the set contains only unique values, duplicates are ignored.
        '''
        return len(set(s))


        '''
        You can also create a dictionary with unique characters as keys and their number in the string as values. 
        The dictionary's length will return a number of elements equal to the number of unique characters in the string.

        d = {}

        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        return len(d)
        '''