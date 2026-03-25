class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        # Using the method .join() we transform the list elements into a single string.
        word1_new = ''.join(word1)
        word2_new = ''.join(word2)

        # If the received strings are equal, then we return true, otherwise we return false
        if word1_new == word2_new:
            return True
        else:
            return False