class Solution:
    def maxDifference(self, s: str) -> int:
        '''
        To find the maximum difference, 
        it is necessary to determine the maximum odd frequency of the symbol 
        and the minimum even frequency
        '''

        # we create variables to search for extremes
        odd_max = 0
        even_min = float('inf')
        d = {}

        # Using a dictionary, we determine the frequency of each character in a string
        for char in s: 
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        # we check each frequency found
        for freq in d.values():

            # If the frequency is even, then we determine the minimum value
            if freq % 2 == 0:
                even_min = min(even_min, freq)

            # for an odd frequency we determine the maximum value
            else:
                odd_max = max(odd_max, freq)

        return odd_max - even_min