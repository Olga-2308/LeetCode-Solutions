class Solution:
    def minLength(self, s: str) -> int:
        
        new_s = ""

        for char in s:

            # we add one character at a time to a new line
            new_s += char

            # After each addition, we check whether the last two characters are the required substrings.
            if new_s.endswith("AB") or new_s.endswith("CD"):

                # we update the string by cutting from the beginning to the end, not including the last two characters
                new_s = new_s[:-2]

        return len(new_s)