class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:

        #  We check each pair of characters in line 6 and specify -1 to avoid going out of bounds.
        for i in range(len(s) - 1):

            # If the absolute value of the difference between two adjacent numbers exceeds 2, 
            # then we immediately return false and terminate the loop. 
            # Converting a symbol to a number for arithmetic calculations
            if abs(int(s[i]) - int(s[i+1])) > 2:
                return False

        # If after checking all pairs of numbers are suitable, then we return true
        return True