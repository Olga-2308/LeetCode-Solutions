class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        result = []
        j = 0
        sp = len(spaces)

        # Using a loop and two pointers, we check the indices 
        # and look for places where spaces need to be added between words
        for i in range(len(s)):

            # Each time we check whether the space pointer has gone beyond the array boundary 
            # and look for the place in the string where a space is needed
            if j < sp and i == spaces[j]:

                # add a space and increment the pointer by one, 
                # moving on to the search for the next space
                result.append(" ")
                j += 1

            # If the space location is not found, then simply add the characters from the string one by one
            result.append(s[i])

        return "".join(result)