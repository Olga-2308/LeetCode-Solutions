class Solution:
    def reverseByType(self, s: str) -> str:
        '''
        We need to return a modified string in which the letters and special characters are in reverse order. 
        To do this, we sort the characters of the original string, reverse the resulting arrays, 
        and compose a string from the characters in the new order.
        '''

        special_characters = "!@#$%^&*()"

        letters = []
        symbols = []

        # Using a loop, we sort the characters of a string into arrays of letters and special characters.
        for char in s:
            if char not in special_characters:
                letters.append(char)
            else:
                symbols.append(char)

        # reverse the resulting arrays so that the elements are in the correct order.
        let = letters[::-1]
        sym = symbols[::-1]

        # create index pointers to insert characters one by one into the resulting list.
        indx_l = 0
        indx_s = 0

        result = []

        # using a loop we return the elements to their place, but in reverse order, 
        # after insertion we increase the corresponding index by 1 to move on to the next element in further iterations
        for char in s:
            if char in special_characters:
                result.append(sym[indx_s])
                indx_s += 1
            else:
                result.append(let[indx_l])
                indx_l += 1

        # we return the received string, as specified in the problem statement
        return "".join(result)