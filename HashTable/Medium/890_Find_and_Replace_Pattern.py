class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        result = []

        d1 = {}
        r1 = []
        indx1 = 0

        # To compare words, they need to be converted into identical digital samples. 
        # We'll use a given string as a sample.
        for char in pattern:

            # If the symbol is not in the string, then we add it to the dictionary and assign it a unique number
            if char not in d1:
                d1[char] = indx1

                # we increment the variable to get a new number
                indx1 += 1

            # We add each number to the dictionary one by one. 
            # Now, instead of comparing letters of the alphabet, we'll compare unique numbers. 
            # For example, aab = 001
            r1.append(d1[char])

        # Now we need to determine which words in the array match the pattern.
        for word in words:

            d2 = {}
            r2 = []
            indx2 = 0

            # To do this, we also transform each word in the array into a digital pattern in the loop.
            for char in word:
                if char not in d2:
                    d2[char] = indx2
                    indx2 += 1
                r2.append(d2[char])

            # If the digital patterns of a pair of words match, then we add this word to the final array
            if r1 == r2:
                result.append(word)

        return result