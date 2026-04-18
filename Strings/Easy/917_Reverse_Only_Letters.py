class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        # Create an empty string for letters only
        chars = ''

        # create a loop in which we check each character and add the letters to a separate line.
        for char in s:
            if char .isalpha():
                chars += char

        # Reverse the resulting string so that the letters are in the correct places.
        revers_chars = chars[::-1]

        # We turn the original string into a list so that we can change the elements, 
        # and create a variable that will point to the index of the character in the created string.
        l = list(s)
        indx = 0

        # 
        for i in range(len(l)):
            if l[i] .isalpha():
                l[i] = revers_chars[indx]
                indx += 1

        #
        return ''.join(l) 