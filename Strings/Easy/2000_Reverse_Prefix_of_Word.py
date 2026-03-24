class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        # We create a loop in which we iterate over the characters by index.
        for i in range(len(word)):

            # If we find a symbol equal to the given one, then the following is done:
            if word[i] == ch:

                # we create the first slice from the beginning of the string up to and including the first found character
                part = word[:i+1]

                # we reverse this slice
                revers_part = part[::-1]

                # ''' As a result, we write a string that consists of the resulting slice and the second slice, 
                # which is the remainder of the original word, starting from the symbol after -ch and to the end '''
                result = revers_part + word[i+1:]

                return result
                
        return word