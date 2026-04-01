class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        # We create a counter for counting inappropriate words.
        counter = 0

        # find the length of a list of words
        l = len(words) 

        # We create a nested loop in which we consider each word from the list.
        for word in words:

            # in the second cycle we consider each symbol in the word
            for char in word:

                # If the symbol is not in the given string, 
                # then we increase the counter by 1 and stop checking the word 
                # and move on to the next word from the list
                if char not in allowed:
                    counter += 1
                    break

        # To find the number of suitable words (which are all those in which no unsuitable characters were found during the loop), 
        # subtract the number of unsuitable words from the total length
        return l - counter 