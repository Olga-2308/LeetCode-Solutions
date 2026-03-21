class Solution:
    def isPalindrome(self, s: str) -> bool:

        # create a new string
        result = ''

        # ''' We create a loop and check each character of the lines. 
        # If the character is a letter or number, then add it to a new string'''
        for char in s:
            if char.isalnum():
                result += char

        # convert all characters of the resulting string to lowercase
        result_low = result.lower()

        # reverse the string and compare it with the original
        if result_low == result_low[::-1]:
            return(True)
        else:
            return(False)