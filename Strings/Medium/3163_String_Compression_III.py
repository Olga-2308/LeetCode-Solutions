class Solution:
    def compressedString(self, word: str) -> str:

        # we create an empty array into which we will add strings one by one
        comp = []

        # we create an empty string in which we will create current lstringsines
        prefix = ""

        # using a loop we add characters one by one
        for char in word:

            # To start checking the prefix, you need to check if it is empty
            if prefix:

                # If the prefix length is less than 9 and consists of identical characters 
                # (including the current character), then we continue adding characters to the prefix
                if len(prefix) < 9 and char in prefix:
                    prefix += char

                # as soon as the prefix exceeds or becomes equal to the set length 
                # or in the iteration a character is different from the character in the prefix, 
                # then we add in turn the number of characters that were in the substring 
                # (the length of the prefix) and the character that this prefix consists of
                elif len(prefix) >= 9 or char not in prefix:
                    comp.append(str(len(prefix)))
                    comp.append(prefix[-1])

                    # clear the substring for new characters
                    prefix = ""

                    # add the current distinct character to an empty string
                    prefix += char

            # If the current line is empty, then we add a symbol to it
            else:
                prefix += char

        # since the remainder may be less than 9 in length, 
        # you must add the remaining part of the string to the result at the end yourself
        comp.append(str(len(prefix)))
        comp.append(prefix[-1])

        return "".join(comp)