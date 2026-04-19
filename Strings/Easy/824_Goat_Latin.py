class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        '''
        A properly formatted string must be returned. 
        To transform each word, the string must be converted into a list of words, allowing for individual word processing. 
        We modify each word according to the problem statement and return the formatted sentence as a string.
        '''

        result = []
        # Create a vowel string to search for letters in a string
        vowels = 'aeiouAEIOU'

        # We turn the string into a list of words so we can work with each word individually.
        l = sentence.split()

        # We set the counter for the number of words in a sentence to write the correct number of letters "a"
        char = 1

        # We create a loop in which we check each word in the list. If the word begins with a vowel, we add "ma"
        for word in l:
            if word[0] in vowels:
                new_word = word + 'ma'
            # If a word begins with a consonant, we move this letter to the end of the word through the slices and add "ma"
            else:
                new_word = word[1:] + word[0] + 'ma'
            
            # At the end of each word, add the letter "a" in accordance with the ordinal number of the word in the sentence.
            new_word += 'a' * char
            result.append(new_word)
            char += 1

        #
        return ' '.join(result)