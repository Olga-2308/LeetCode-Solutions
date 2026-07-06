class Solution:
    def reformat(self, s: str) -> str:

        alpha = ''
        digit = ''

        # we count the number of letters and numbers in a string
        for char in s:
            if char.isalpha():
                alpha += char
            else:
                digit += char

        # If the difference between the number of letters and numbers is greater than 1, 
        # this means that it is impossible to create a permutation in which two adjacent symbols 
        # will not be of the same type, since due to the predominance of one of the types, 
        # two numbers or two letters will go together in some part of the line
        possible = abs(len(alpha) - len(digit))
        if possible > 1:
            return ''

        result = ''

        # If the number of letters is greater than the number of digits, 
        # then we start composing the string with letters so that there are no trailing letters, 
        # and at the end we add the last letter that was not in the loop to the result
        if len(alpha) > len(digit):

            # using a loop we form a new string and return the result 
            # and add the last character to the string, if there is one left
            for i in range(len(digit)):
                result += alpha[i] + digit[i]
            return result + alpha[len(digit):]

        # We create a new line in the same way, 
        # but only if the number of letters is greater than or equal to the number of numbers
        else:
            for i in range(len(alpha)):
                result += digit[i] + alpha[i]
            return result + digit[len(alpha):]