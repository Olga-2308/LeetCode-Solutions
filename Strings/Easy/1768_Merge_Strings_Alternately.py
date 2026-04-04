class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # we create an empty string into which we will add characters in the specified order
        res = ''

        # We find a line with the minimum number of characters to determine the boundary of the loop and not go beyond the limit
        m = min(len(word1), len(word2))

        # We create a loop in which we add characters from two lines one by one
        for i in range(m):
            res += word1[i] + word2[i]

        # After the loop has completed, there may be some remaining characters in the original string, 
        # as the strings can be of different lengths. 

        # Therefore, after adding a new string, any remaining characters from the original strings must be added.

        # Therefore, we specify slices from the final value of the loop (the number m was not included in the loop, 
        # but it is included at the beginning of the slice) to the end of the string. 
        
        # If any characters remain in any of the strings, they will be added to the end of the new string.
        result = res + word1[m:] + word2[m:]

        return result  