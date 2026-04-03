class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        # We create a counter for counting broken words.
        counter = 0

        # converting a string into a list of words
        words = text.split()

        # create list and separate the characters to check each one for compliance
        symbols = list(brokenLetters)

        # take the first word from the list of words
        for word in words:
            # and we take the first symbol
            for char in symbols:

                # If this symbol is in the word, it means the word is broken and we increase the counter by one.
                if char in word: 
                    counter += 1
                    # interrupt the current loop as soon as we find one character in the word
                    break

        # To find the number of matching words, you need to subtract the broken words 
        # that were found and counted in the loop from the total number of words
        result = len(words) - counter

        return result