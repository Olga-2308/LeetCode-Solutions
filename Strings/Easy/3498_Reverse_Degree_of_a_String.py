class Solution:
    def reverseDegree(self, s: str) -> int:

        indx = 1
        total = 0

        for char in s:

            # Since it is necessary that the ordinal number of the letter of the alphabet be in reverse order, 
            # it is necessary to determine such a number, when subtracting the ordinal number of the symbol from which, 
            # the difference will be equal to the expanded ordinal number of the alphabet
            product = (123 - ord(char)) * indx # a(97), z(122)
            total += product
            indx += 1

        return total