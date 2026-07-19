class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        '''
        It's necessary to return the minimum cost of moves. So, moving to an adjacent cell costs 1, 
        and moving 1 beyond costs 0. Therefore, it's necessary to move numbers strictly according to their indexes. 
        But to ensure all coins are in the same cell, 
        it's necessary to move all coins from an even index to an odd index or vice versa. 
        To obtain a lower cost, you need to move the coins that are fewer in number on even or odd indexes.
        '''

        even = 0
        odd = 0

        for num in position:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

        return min(even, odd)