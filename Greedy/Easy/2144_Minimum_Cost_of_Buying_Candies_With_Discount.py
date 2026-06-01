class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        '''
        To pay the minimum price for all the candies, you need to buy the two most expensive candies, 
        then take the most expensive one from the remaining ones for free.
        '''

        total = 0

        # We sort the array in descending order so that we can buy candies one by one 
        # and take the most expensive ones every third candy in turn.
        cost.sort(reverse = True)

        # If there are 2 or fewer candies in the array, then you can only buy them all
        if len(cost) <= 2:
            return sum(cost)

        # Using a loop, we buy all the candies one by one, except for every third one. 
        # The indices are ordered and, in normal ordinal counting, 
        # every third number is divisible by 3 (3, 6, 9, 12, etc.). 
        # However, since array indexing starts at 0, one must be added to the index to determine divisibility.

        # [0] 2
        # [1] 3
        # [2] 1
        # [3] 2
        # [4] 4
        
        # For example, we need to take the third candy - this is a candy worth 1, which we can take for free.        
        # This candy is indexed 2.
        # And in the current iteration we add 1 to the index 
        # and get a value that is divisible by three without a remainder.
        # If we get a remainder when dividing, this means that the candy is not every third one and we buy it 
        # (we add it to the total cost variable)

        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total += cost[i]

        return total