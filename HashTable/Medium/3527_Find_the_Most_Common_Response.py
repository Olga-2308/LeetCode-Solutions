class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        total = {}

        # Using a loop, we determine the frequency of each word in the array.
        for words in responses:

            # Before recording the frequency of words, 
            # each subarray must be cleared of duplicates, for this we use a set
            unique = set(words)

            for word in unique:
                if word not in total:
                    total[word] = 1
                else:
                    total[word] += 1

        max_freq = 0
        small_word = ""

        # Now that we know the frequency of unique words in each subarray, 
        # we need to determine the most frequent and at the same time the minimum word 
        # (if there are several words with the same maximum frequency)
        for word, freq in total.items():

            # If the frequency of a word is greater than the previously set frequency, 
            # then the frequency and the word are updated
            if freq > max_freq:
                max_freq = freq
                small_word = word

            # If you encounter a word with the same frequency, 
            # you need to determine which word is less frequent and 
            # leave it in the variable or replace it if the current one turns out to be less frequent
            elif freq == max_freq:
                if word < small_word:
                    small_word = word

        return small_word