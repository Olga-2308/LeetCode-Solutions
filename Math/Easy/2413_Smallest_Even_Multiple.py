class Solution:
    def smallestEvenMultiple(self, n: int) -> int:

        # ''' We create a loop that will check each number in turn to see if the conditions are met. 
        # We start with 1, because we need to return a positive number, 
        # and work our way up to 2n + 1 
        # (the common multiple of n and 2 will definitely not exceed 2n + 1 to reach the final value). '''
        for i in range(1, n*2+1):

            # we find the smallest positive integer that is a multiple of both 2 and n
            if i % 2 == 0 and i % n == 0:
                
                # return the result
                return i