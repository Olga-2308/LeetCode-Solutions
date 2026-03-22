class Solution:
    def isValid(self, word: str) -> bool:
        # create strings with vowels and consonants of the English alphabet, taking into account the case of letters
        vowels = "aeiouAEIOU"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        Flag = True


        # we check the first condition - the number of characters, if the condition is not met, false is returned
        if len(word) < 3:
            return False
        
        # we check the following condition - the line must contain only letters and numbers, if the condition is not met, false is returned
        if not word.isalnum():
            return False

        has_vowel = False
        has_consonant = False
        
        # create a loop and check whether the string contains a vowel letter, and whether the string contains a consonant letter
        for char in word:
            if char in vowels:
                has_vowel = True
            elif char in consonants:
                has_consonant = True
        
        # the condition is satisfied if the string has both a consonant and a vowel at the same time
        if has_vowel == True and has_consonant == True:
            return True
        else:
            return False