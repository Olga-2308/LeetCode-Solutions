class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        d = {}
        current = 0
        max_string = -1

        # If the length of a string is equal to the length of a set of the same string, 
        # this means that there are no two identical characters in the string, and we return -1
        if len(s) == len(set(s)):
            return -1

        # Find the length of a substring between two identical characters using a loop
        for i in range(len(s)):

            # If a symbol is not in the dictionary, 
            # it means it is its first occurrence and we write down its index
            if s[i] not in d:
                d[s[i]] = i

            else:
                # If the symbol is already in the dictionary, then we can find the length of the substring 
                # between two identical symbols by determining the difference between the current index 
                # and the index of the same symbol written earlier
                current = i - d[s[i]] - 1

                # and each time we determine the maximum length
                if current > max_string:
                    max_string = current

        return max_string
        