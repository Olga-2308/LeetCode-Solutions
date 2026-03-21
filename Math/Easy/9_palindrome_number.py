class Solution:
    def isPalindrome(self, x: int) -> bool:

        # turn a number into a string
        s = str(x)

        # reverse the string and compare it with the original string
        if s == s[::-1]:
            return(True)
        else:
            return(False)