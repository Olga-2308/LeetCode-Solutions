class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        '''
        Words in an array can be made equal through an unlimited number of permutations 
        only if the frequency of each letter in the array is divisible by the length of the array without a remainder.
        '''

        l = len(words)
        d = {}

        # In the dictionary, we fill in the frequencies of all letters that appear in the array of words
        for word in words:
            for char in word:
                if char not in d:
                    d[char] = 1
                else:
                    d[char] += 1

        # We check each received frequency number in the dictionary, as soon as the division condition is not met, 
        # we return false, since it is impossible to make the words equal
        for char, freq in d.items():
            if freq % l != 0:
                return False

        return True