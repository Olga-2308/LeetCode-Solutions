class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        # create a counter to count the number of pairs of strings
        counter = 0

        # create a nested loop in which we work with pairs of words
        for i in range(len(words)):

            # shift the second cycle by one so that the words do not repeat, 
            # and the condition i <j will also be satisfied.
            for j in range(i+1, len(words)):

                # revers the second word and compare the pair of words. 
                # If the words are the same, we increase the counter by 1.
                if words[i] == words[j][::-1]:
                    counter += 1

        return counter