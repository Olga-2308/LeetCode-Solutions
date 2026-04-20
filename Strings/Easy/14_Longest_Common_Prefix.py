class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        '''
        The prefix can't be longer than the minimum word, so we find the shortest string in the array to compare characters against. 
        In the outer loop, we take the first letter of the short word, 
        and in the inner loop, we compare this character with all the other characters in the words 
        at the corresponding indices and record all matches. Once there are no more matches, we return the resulting string.
        '''

        result = ''

        # We find the shortest word by which we will search for a common prefix
        prefix = min(strs)

        # In the outer loop, we define a variable with which we will compare the letters in the remaining words.
        for i in range(len(prefix)):
            char = prefix[i]

            # In the inner loop, we compare all the characters under the current index, 
            # and if there is a match, we add the character to the final string; otherwise, we return the resulting value.
            for word in strs:
                if word[i] != char:
                    return result

            result += char

        return result