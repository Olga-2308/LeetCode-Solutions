class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        d1 = {}
        d2 = {}
        counter = 0

        # We determine the frequency of each word in the first array
        for word in words1:
            if word not in d1:
                d1[word] = 1
            else:
                d1[word] += 1

        # We determine the frequency of each word in the second array
        for word in words2:
            if word not in d2:
                d2[word] = 1
            else:
                d2[word] += 1

        # To check which words appeared once in each array, 
        # you need to create a loop and check each word from the first dictionary.
        for word, freq in d1.items():
            
            #We need a word that appears once in the first dictionary, 
            # and also for the same word to be in the second array, 
            # where its frequency is also equal to 1. 
            # If such a word is found, we increment the counter
            if freq == 1 and word in d2 and d2[word] == 1:
                counter += 1

        return counter

        '''
        d = {}
        counter = 0

        for word in words1:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

        for word in words2:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

        for word, freq in d.items():
            if freq == 2 and word in words1 and word in words2:
                counter += 1

        return counter
        '''