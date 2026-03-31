class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        # create a counter to count the number of words that start with a prefix.
        counter = 0

        # create a loop in which we check each word in order
        for word in words:

            # If the word begins with the specified prefix, then increase the counter by 1
            if word.startswith(pref):
                counter += 1

        return counter