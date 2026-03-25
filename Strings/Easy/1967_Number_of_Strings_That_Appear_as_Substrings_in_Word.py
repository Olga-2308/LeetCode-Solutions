class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        # create a counter in which we will count the number of substrings
        counter = 0

        # create a loop in which we check each string to see if it is a substring in word
        for s in patterns:
            if s in word:
                counter += 1

        return counter