class Solution:
    def scoreOfString(self, s: str) -> int:

        score = 0

        # create a loop in which we perform actions with each element in order (-1 to avoid going beyond the bounds)
        for i in range(len(s)-1):

            # find the absolute value of the difference between two adjacent elements
            mod = abs(ord(s[i]) - ord(s[i+1]))

            # find the sum of the numbers
            score += mod

        return score