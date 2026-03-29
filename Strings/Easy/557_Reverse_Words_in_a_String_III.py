class Solution:
    def reverseWords(self, s: str) -> str:

        # create a list for inverted words
        words = []

        # converting a string into a list
        new = s.split()

        # we create a loop in which we work with each word
        for i in range(len(new)):

            # reverse the word
            rev = new[i][::-1]

            # add a word to the list
            words.append(rev)

        # converting the list back to a string
        result = ' '.join(words)

        return result