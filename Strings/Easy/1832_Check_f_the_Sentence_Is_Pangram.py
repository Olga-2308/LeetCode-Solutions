class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        # create a string with the English alphabet in lowercase.
        alph = 'abcdefghijklmnopqrstuvwxyz'

        # ''' We create a loop in which we check each letter of the alphabet. 
        # If one of the characters is not in the given string, we return false; 
        # otherwise, we return true. '''
        for char in alph:
            if char not in sentence:
                return False
        
        return True