class Solution:
    def replaceDigits(self, s: str) -> str:

        result = ""

        for i in range(len(s)):

            # If the current character is a letter, then we simply write it to the string without changes.
            if s[i] .isalpha():
                result += s[i]

            # If the current character is a digit, it must be replaced with a letter according to the rule in the problem statement. 
            # We find the sum of the ordinal number of the previous character and the current one 
            # (convert the character to a number for arithmetic operations) 
            # and return the character that corresponds to the resulting ordinal number.
            else:
                char = chr(ord(s[i-1]) + int(s[i]))
                result += char

        return result