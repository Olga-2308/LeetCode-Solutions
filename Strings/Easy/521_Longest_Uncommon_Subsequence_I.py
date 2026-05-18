class Solution:
    def findLUSlength(self, a: str, b: str) -> int:

        # If the strings are equal, then return -1
        if a == b:
            return -1

        # If the strings are different, then we return the length of the maximum string
        else:
            return max(len(a), len(b))