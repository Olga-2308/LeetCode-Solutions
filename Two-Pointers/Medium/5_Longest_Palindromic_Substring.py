class Solution:
    def longestPalindrome(self, s: str) -> str:

        # If given an empty string, then return an empty string.
        if len(s) == 0:
            return ""

        # We create two variables, where in the final one we set the first value of the string 
        # to return the character if the palindrome is not found.
        max_palindrom = s[0]
        current_palindrom = ""

        # we create a loop in which each time we move the current symbol to the center of the palindrome
        for i in range(len(s)):

            '''
            In the first case, the center of the palindrome can be one letter, 
            then it is necessary to compare the characters to the right and left of the center
            '''

            # Find the left and right symbols from the center one
            left = i - 1
            right = i + 1

            # in the next cycle we expand the boundaries of the palindrome until either we go beyond one of the boundaries 
            # and there is nowhere else to expand, or until the symbols are no longer equal, which means the end of the palindrome
            while  left >= 0 and right < len(s) and s[left] == s[right]:

                # If we are in a loop, then the symbols are the same and we update the current value
                current_palindrom = s[left:right+1]

                # We determine the maximum palindrome
                if len(current_palindrom) > len(max_palindrom):
                    max_palindrom = current_palindrom

                # After we have written down a new palindrome, 
                # we move one to the right and one to the left and start checking the symbols again.
                left -= 1
                right += 1

            '''
            In the second case, the center of the palindrome can be two identical symbols
            '''

            # These characters are defined as the current character from the loop (left) and the adjacent character in the string (right)
            left = i
            right = i + 1

            # We also check paired symbols and look for the maximum palindrome.
            while  left >= 0 and right < len(s) and s[left] == s[right]:
                current_palindrom = s[left:right+1]
                if len(current_palindrom) > len(max_palindrom):
                    max_palindrom = current_palindrom

                left -= 1
                right += 1

        return max_palindrom