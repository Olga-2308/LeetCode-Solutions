class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        # create a loop in which we iterate over each string of the list in order
        for s in words:

            # check whether the original string is equal to the string in expanded form (the palindrome condition)
            if s == s[::-1]:

                # if the condition is met, then we return this string
                return s

        return ""