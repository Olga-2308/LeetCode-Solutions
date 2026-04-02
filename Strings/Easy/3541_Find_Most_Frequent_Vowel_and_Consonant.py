class Solution:
    def maxFreqSum(self, s: str) -> int:

        # create two lines with vowels and consonants separately to split the check into two parts.
        vovels = 'aeiou'
        consonant = 'bcdfghjklmnpqrstvwxyz'

        # We create an empty list to which we'll add characters that have already been checked in the loop. 
        # Since characters in the string can be repeated, the loop will have to recalculate their number. 
        # If we add a checked character to the list and specify in the loop that it should be skipped, 
        # further checks will only be performed on unique characters.
        check_chars = []

        # We create two variables to find the maximum values.
        max_count_vowel = 0
        max_count_consonant = 0

        # We create a loop in which we check each character in the string.
        for char in s:

            # If the symbol is among the vowels and has not been checked before, then:
            if char in vovels and char not in check_chars:

                # we count the number of repetitions of this symbol in the string
                count = s.count(char)

                # add this symbol to the list of verified ones
                check_chars.append(char)

                # If the number of characters is greater than the maximum value, then we update this maximum value
                if count > max_count_vowel:
                    max_count_vowel = count

            # create exactly the same cycle and check for all consonants in the string
            elif char in consonant and char not in check_chars:
                count = s.count(char)
                check_chars.append(char)
                if count > max_count_consonant:
                    max_count_consonant = count

        # find the sum of the maximum values
        result = max_count_vowel + max_count_consonant

        return result 