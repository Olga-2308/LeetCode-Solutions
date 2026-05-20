class Solution:
    def isValid(self, s: str) -> bool:

        new_s = []

        for char in s:

            # we add one character at a time to the array
            new_s.append(char)

            # We start checking the subarray only when the array has at least three elements
            if len(new_s) >= 3:

                # If the elements "a", "b", "c" are at the end of the array, 
                # then we delete them and continue adding new characters
                if new_s[-1] == "c" and new_s[-2] == "b" and new_s[-3] == "a":
                    new_s.pop()
                    new_s.pop()
                    new_s.pop()                

        # If the length is 0, then all characters have been removed and the string is valid.
        return len(new_s) == 0