class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        To optimally distribute cookies between the required ones, 
        it is necessary to satisfy the minimum requirement with the minimum possible number of cookies.
        '''

        # We sort the arrays to start distributing cookies optimally among the children.
        g.sort()
        s.sort()
        counter = 0

        # we set pointers to the beginning of each array
        i = 0
        j = 0

        while i < len(g) and j < len(s):

            # If the child's greed is equal to or less than the current minimum cookie size, 
            # then we can satisfy the greed of that child, make a pair, 
            # and move on to finding the next one by moving the pointers one step to the right
            if g[i] <= s[j]:
                counter += 1
                i += 1
                j += 1

            # If the child's greed is higher, 
            # then we need to look for a new size of cookie until it suits the child.
            else:
                j += 1

        return counter