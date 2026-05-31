class Solution:
    def repeatedCharacter(self, s: str) -> str:

        d = {}

        for char in s:

            # If the symbol is not in the dictionary, then we add it to the dictionary
            if char not in d:
                d[char] = 1

            # If the symbol is already in the dictionary, 
            # we immediately return the first duplicate we encountered.
            else:
                return char