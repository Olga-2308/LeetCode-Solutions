class Solution:
    def greatestLetter(self, s: str) -> str:

        # we turn the string into many unique characters to reduce verification time
        word = set(s)
        result =  ""

        # We check each character in the set of unique letters; 
        # if the character is present in both registers in the string, 
        # we return the maximum of them (if there are several such characters)
        for char in word:
            if char.lower() in word and char.upper() in word:
                result = max(result, char.upper())

        return result