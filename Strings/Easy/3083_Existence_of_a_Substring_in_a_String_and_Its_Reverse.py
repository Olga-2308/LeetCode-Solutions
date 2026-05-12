class Solution:
    def isSubstringPresent(self, s: str) -> bool:

        # We create an expanded string in which we will check for substring matches
        ss = s[::-1]

        # using a loop we create substrings of length 2 elements
        for i in range(len(s) - 1):
            sub = s[i] + s[i+1]

            # If the resulting substring is in the expanded string, then return true
            if sub in ss:
                return True

        return False
    

        '''
        d = {}
        ss = s[::-1]

        for i in range(len(s) - 1):
            sub = s[i] + s[i+1]
            if sub not in d:
                d[sub] = 1
            else:
                d[sub] += 1

        for i in range(len(ss) - 1):
            sub = ss[i] + ss[i+1]
            if sub in d:
                return True

        return False
        '''