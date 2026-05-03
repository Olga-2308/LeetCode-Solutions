class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # We define the string length to specify the loop limit. 
        # Since every letter must be checked, the number of offsets equals the number of letters in the string.
        l = len(s)

        while l > 0:

            # If the strings are equal, then we terminate the loop and return true.
            if s == goal:
                return True
            
            # If the strings are not equal, then we create a new string from the slices, 
            # where the first character goes to the end of the string and shorten the loop step
            else:
                s = s[1:] + s[0]
                l -= 1

        # If the strings cannot be made equal, then return false
        return False