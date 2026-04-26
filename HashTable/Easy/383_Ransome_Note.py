class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        counter = {}

        # We create a loop in which we count the number of each letter in the string.
        for letters in magazine:

            # If the letter is already in the dictionary, then we increase the counter by 1
            if letters in counter:
                counter[letters] += 1
            
            # if there is no letter, then create a new record with the value 1
            else:
                counter[letters] = 1

        # In the second loop, we check whether it is possible to create a string from the letters that are in the dictionary (the first string)
        for symbols in ransomNote:

            # We check if this symbol is in the dictionary.
            if symbols in counter:

                # If the symbol is in the dictionary, then we subtract 1 from the value to get the current remainder.
                if counter[symbols] > 0:
                    counter[symbols] -= 1

                # If there is no symbol, then it is impossible to create a string, and then we immediately return false
                else:
                     return False
            else:
                return False

        return True