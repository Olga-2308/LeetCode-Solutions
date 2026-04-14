class Solution:
    def countSegments(self, s: str) -> int:

        # Using the split method, we turn the string into an array of words, with spaces serving as word separators.
        res = s.split()

        # Once we have created an array of words, we can immediately determine the number of segments
        result = len(res)

        return result