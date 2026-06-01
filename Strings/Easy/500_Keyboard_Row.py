class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        # We create sets for each row of the keyboard for quick character searches.
        one = set('qwertyuiop')
        two = set('asdfghjkl')
        three = set('zxcvbnm')

        result = []

        # We check each word in the array, 
        # since the lowercase and uppercase letters correspond to the same key, 
        # we write the word in lowercase using the method
        for word in words:
            pattern = []
            w = word.lower()

            # We check each character in the resulting word 
            # and add to the array the number corresponding to the keyboard row for each character.
            for char in w:
                if char in one:
                    pattern.append(1)
                elif char in two:
                    pattern.append(2)
                elif char in three:
                    pattern.append(3)

            # We transform the array into a set and find its length. 
            # If the array length is greater than one, 
            # this means that the word was typed using several rows of the keyboard. 
            # If the length is 1, then the word was written in one row 
            # and we add the original word to the result.
            if len(set(pattern)) == 1:
                result.append(word)

        return result