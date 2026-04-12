class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If words are anagrams, they consist of the same letters. 
        # To determine whether words are anagrams, you need to compare their symbols.

        # First, we convert the strings into character arrays so that we can change the elements
        ss = list(s)
        tt = list(t)

        # then we sort the resulting arrays
        ss.sort()
        tt.sort()

        # If the resulting arrays are equal after sorting, 
        # then the original words are anagrams and true is returned, 
        # otherwise false is returned.
        return ss == tt