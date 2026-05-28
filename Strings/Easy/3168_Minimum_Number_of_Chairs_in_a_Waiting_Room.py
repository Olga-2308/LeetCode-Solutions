class Solution:
    def minimumChairs(self, s: str) -> int:
        '''
        Since guests arrive and leave randomly, the number of available chairs required varies each time. 
        To determine the minimum number of chairs needed for all guests, 
        you need to identify the time when the largest number of guests will be present 
        and when they will all need chairs, at a minimum.
        '''

        total = 0
        result = 0

        # using a loop, we alternately record the number of guests who arrived and left
        for char in s:

            # If a person arrives, then we add one place and determine the maximum value
            if char == "E":
                total += 1
                result = max(result, total)

            # If a person leaves, then we subtract 1, and this means that one seat is free, 
            # and when new guests arrive, we will not add extra chairs.
            else:
                total -= 1
        
        return result