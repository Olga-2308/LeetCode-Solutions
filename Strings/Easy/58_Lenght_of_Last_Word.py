class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # turn the string into an array so that we can work with the elements individually.
        new_s = s.split()

        # find the length of the last element at index -1
        result = len(new_s[-1])

        return result