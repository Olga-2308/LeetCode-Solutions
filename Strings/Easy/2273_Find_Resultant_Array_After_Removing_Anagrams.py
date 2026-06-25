class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        '''
        Anagrams are words that contain the same set of characters; to check if words are anagrams, 
        it is necessary to sort the characters lexicographically and compare them.
        '''

        # The first word will always be the result, since in the event of a match, 
        # the word further to the right (with the highest index) must be removed.
        w = sorted(words[0])

        result = [words[0]]
        sort_words = [w]

        # We use a loop to check the remaining words in sorted order.
        for i in range(1, len(words)):
            word = sorted(words[i])
            
            # If the current word is not an anagram of the last word in the result, 
            # it is added to the result and becomes the new starting point for checking all subsequent words; 
            # therefore, we add its sorted version for comparison purposes and add the original word to the result.
            if word != sort_words[-1]:
                sort_words.append(word)
                result.append(words[i])

        return result