class Solution:
    def finalString(self, s: str) -> str:

        # create an empty list with which we will perform the reversal
        res = []

        # create a loop in which we go through each element of the string
        for char in s:

            # If the symbol is equal to the letter "i", then the list is expanded
            if char == 'i':

                # with this action we expand the list
                res = res[::-1]
            else:
                # otherwise, we simply add the symbol to a new list
                res.append(char)

        # since we were working with a list and needed to return a string, we used a method to convert the list into a string.
        result = ''.join(res)
        
        return result