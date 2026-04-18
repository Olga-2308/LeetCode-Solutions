class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        '''
        We create a row variable from which the filling begins
        '''
        row = 1

        '''
        We create a loop in which we fill rows until there are fewer coins than spaces in the row:
            - fill the current row and find the number of remaining coins
            - move to the next row, which is one more than the previous one
        '''
        while n >= row:
            n -= row
            row += 1

        '''
        As soon as there aren't enough coins to completely fill a row, 
        we exit the loop and find the number of completely filled rows.

        Since in the loop we incremented the row each time after the previous filling, 
        to find completely filled rows, we need to subtract 1—the row that isn't completely filled.
        '''
        result = row - 1

        return result