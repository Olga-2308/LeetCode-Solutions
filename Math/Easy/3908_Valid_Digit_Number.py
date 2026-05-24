class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        '''
        To quickly determine whether a number is valid, 
        you need to convert all numbers into strings and check the required characters individually
        '''

        # converting numbers into strings
        num = str(n)
        xx = str(x)

        # a number is valid if it does not start with the specified digit, 
        # but this digit is present in the number being checked
        return num[0] != xx and xx in num