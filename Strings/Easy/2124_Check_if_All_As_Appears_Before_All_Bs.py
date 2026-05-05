class Solution:
    def checkString(self, s: str) -> bool:

        for i in range(len(s)):

            # We create a loop in which we check each character; 
            # if we encounter the letter "a", we skip it.
            if s[i] == "a":
                continue

            # As soon as you encounter the letter "b", 
            # you need to check the rest of the line for the letter "a"
            elif s[i] == "b":

                # If the letter "a" is found in the remainder of the line, 
                # then we return false, since the condition of the problem is not met
                if "a" in s[i:]:
                    return False

        return True

        '''
        You can also simply check if the letter combination "ba" is in the string. 
        If "a" comes after "b", then we immediately return false.

        if "ba" in s:
            return False
        else:
            return True
        '''