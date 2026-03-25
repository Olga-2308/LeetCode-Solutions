class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:

        # we create a string to which we will add the first letters of the strings
        new_acr = ''

        # we start a loop in which we create a string from the first letters
        for word in words:
            new_acr += word[0]

        # шf the resulting string is equal to the string from the condition, then we return true, otherwise false
        if new_acr == s:
            return True
        else:
            return False