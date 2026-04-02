class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:

        # To find the sum of all permutations between identical symbols from two rows, 
        # you must first determine how many steps it took to move one symbol.

        # we create a variable to count the total number of permutations
        total = 0

        # we create a loop in which we work with each character in order
        for i in range(len(s)):

            # we take the symbol under the current index
            char = s[i]
 
            # and using the method we find the index of the same character in the second line
            second_char = t.find(char)

            # To find the number of movements between two symbols, 
            # you need to find the absolute value of the difference in their indices
            total += abs(i - second_char)

        return total