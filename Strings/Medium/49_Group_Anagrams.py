class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}

        # Using a loop, we distribute words into groups. 
        # To find anagrams, we need to reduce all words to a common form. 
        # To do this, we sort the characters in the string.
        for word in strs:
            w = sorted(word)
            chars = "".join(w)

            # If the resulting set is not yet in the dictionary, 
            # then we write down this set and the original word
            if chars not in d:
                d[chars] = word
            
            # If we encounter a word whose anagram is already in the dictionary, 
            # we add the next word to it, punctuated by a slash. 
            # This creates groups of words in the dictionary that correspond to similar patterns.
            else:
                d[chars] = d[chars] + "'" + word

        result = []

        # We form a list of answers, where anagram words are grouped in each subarray
        for word in d.values():
            w = word.split("'")
            result.append(w)

        return result
        
        '''
        d = {}

        for word in strs:
            w = sorted(word)
            chars = "".join(w)

            if chars not in d:
                d[chars] = []

            d[chars].append(word)

        return list(d.values())
        '''