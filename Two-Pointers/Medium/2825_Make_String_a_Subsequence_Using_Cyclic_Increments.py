class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        '''
        To determine whether a sequence can be formed from the first string, 
        each character from the second string must be tested in turn against all the variations of characters from the first string.
        '''

        i = 0
        j = 0

        # We check the lines until one of them runs out of characters to check.
        while i < len(str1) and j < len(str2):

            # We check the letter z separately, 
            # since when shifted it turns into the first letter of the alphabet, not the next character.
            if (str1[i] == 'z' and str2[j] == 'a'):

                #If the symbols match, then we move on to the next symbol in the sequence 
                # (the symbols in the sequence change only after a match is found)
                j += 1

            # then we look for a match between a character from the sequence 
            # and a character from the original string or its offset by 1 letter forward
            elif str1[i] == str2[j] or chr(ord(str1[i]) + 1) == str2[j]:
                j += 1

            # After each check, we shift the index of the main line forward by 1
            i += 1

        # If after executing the entire loop the index j is equal to the length of the sequence, 
        # then all these letters from the sequence can be composed from the original string
        return j == len(str2)