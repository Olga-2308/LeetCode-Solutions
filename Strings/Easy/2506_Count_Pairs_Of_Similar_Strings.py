class Solution:
    def similarPairs(self, words: List[str]) -> int:
        '''
        To determine whether two strings are similar, 
        you need to find out whether they consist of the same characters 
        (the frequency of the characters is not important, 
        the main thing is that the set of characters is the same in both strings)
        '''

        d = {}
        counter = 0

        # We need to fill the dictionary with words so they can be compared. 
        # To do this, we clear the string of duplicates and sort it in order. 
        # This way, each word will take the same form as a set of characters.
        for word in words:

            # removing duplicates
            p = set(word)

            # sort for further comparison
            pp = sorted(p)

            # Since after sorting a string an array of characters is returned, 
            # we convert the array back into a string
            pattern = "".join(pp)

            # If such a unique set is not in the dictionary, 
            # then we add it to the dictionary
            if pattern not in d:
                d[pattern] = 1
            
            # If the set already exists in the dictionary, then at least one pair exists. 
            # However, we need to determine the number of pairs, since the further the index, 
            # the greater its value, which corresponds to the problem statement (i < j). 
            # It turns out that each new word found from the dictionary forms a pair with every previous word 
            # (and each word increments the dictionary counter). 
            # Therefore, we first determine the number of all possible pairs with the current word, 
            # and then add 1 to this word in the dictionary.
            else:
                counter += d[pattern]
                d[pattern] += 1
                
        return counter