class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        # We create a string of characters that must be in each substring.
        vowels = "aeiou"
        counter = 0

        # We create a nested loop in which we check each substring. 
        # "i" it points to the first letter in the string.
        for i in range(len(word)):

            # We create an empty string, each time we move to a new initial letter of the substring, 
            # we will start composing the string from the beginning
            sub = ""

            # In the inner loop, we will collect the vowels into a string one by one 
            # (starting with i and checking the very first character)
            for j in range(i, len(word)):

                # We build the string until we encounter a consonant. 
                # Once we encounter one, we finish building the substring.
                if word[j] not in vowels:
                    break

                # And if vowels are collected all this time, 
                # then we add them to the line one by one
                if word[j] in vowels:
                    sub += word[j]

                    # And each time we add a vowel, we check whether the current substring is suitable. 
                    # To do this, we check the string against the set and count the number of unique characters. 
                    # If the set's length is equal to the length of the vowel string 
                    # (or the length is 5, since there are only 5 vowels), 
                    # then this means the substring contains all the vowels, 
                    # and we can increment the counter. 
                    # After this, we continue adding vowels to the string (if they are continuous), 
                    # and each time we increment the counter by 1, 
                    # since all the necessary characters are already in the substring.
                    if len(vowels) == len(set(sub)):
                        counter += 1
                    
        return counter