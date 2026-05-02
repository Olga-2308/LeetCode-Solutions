class Solution:
    def trimTrailingVowels(self, s: str) -> str:

        vowels = "aeiou"
        ss = []

        # convert a string into an array of characters
        for char in s:
            ss.append(char)

        # ss = list(s)

        # remove each last letter of the array that is a vowel
        while ss and ss[-1] in vowels:
            del ss[-1]

        # return the string
        return "".join(ss)