class Solution:
    def kthCharacter(self, k: int) -> str:

        # create a string ine with the first letter of the alphabet as the beginning of the game.
        word = 'a'

        # since it is necessary to return a specific character in the string, 
        # then this string must be increased until this character is no longer in the string
        while len(word) < k:

            # create an empty string for new characters, 
            # since the characters of the original string need to be preserved
            new_word = ''

            # create a cycle in which we create a new one for each symbol, according to the problem statement
            for char in word:

                # the new character is the next letter of the alphabet from the current character in the loop
                new_char = chr(1 + ord(char))

                # add the received symbol to the created string
                new_word += new_char

            # add new characters to the original string; if the length of the resulting string has not reached K, 
            # then we continue the cycle and create new characters.
            word = word + new_word

        # we will return the character at a specific location in the string, 
        # since the search for a character specifies the index of the location, and not the serial number in the string, then it is necessary to subtract 1
        return word[k-1]