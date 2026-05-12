class Solution:
    def reverseWords(self, s: str) -> str:

        vowels = set("aeiou")

        # convert a string into an array of strings
        words = s.split()
        result = []

        need = 0

        # we count the number of vowels in the first word
        for char in words[0]:
            if char in vowels:
                need += 1

        # we add the first word to the result in its original form
        result.append(words[0])

        counter = 0

        # using a loop, we count the vowels in each of the remaining words
        for i in range(1, len(words)):
            word = words[i]

            # we count the number of vowels
            for char in word:
                if char in vowels:
                    counter += 1
            
            # If the number of vowels in the current word matches the number of vowels in the first word, 
            # then we add the word to the result in expanded form
            if counter == need:
                result.append(word[::-1])

            # If the number of vowels is different, then we add the word without changes
            else:
                result.append(word)

            # reset the counter for counting vowels in the next word
            counter = 0

        # we return the result as a string
        return " ".join(result)