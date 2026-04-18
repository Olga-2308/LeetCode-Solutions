class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        We need to determine whether the strings are equal after all transformations. 
        To do this, we create lists that will contain all the elements after the necessary transformations. 
        Finally, we check the equality of these lists.
        '''

        # We create empty lists that need to be compared after transformation according to the rules
        ss = []
        tt = []

        # We create a cycle in which we perform actions with each symbol, in accordance with the conditions of the problem
        for char in s:
            # If the symbol is not a '#', then we add it to the list
            if char != '#':
                ss.append(char)
            # And if the hash symbol is a '#', then it is necessary to remove the previous one from the list 
            # (additionally, we check whether the element is in the list)
            else:
                if ss:
                    ss.pop()

        # We create a second list in a similar way.
        for char in t:
            if char != '#':
                tt.append(char)
            else:
                if tt:
                    tt.pop()

        # Compare strings and return a Boolean value
        return ss == tt