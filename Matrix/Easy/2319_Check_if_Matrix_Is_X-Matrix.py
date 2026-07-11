class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        m = len(grid)

        # we determine the initial position of the second diagonal of the matrix, 
        # which is in the upper right corner
        row = 0
        col = m - 1

        # We create a nested loop in which we check each cell of the matrix.
        for i in range(m):
            for j in range(m):

                # Next, we determine the cells of both diagonals of the matrix. 
                # If during the iteration we encounter a cell of one of the diagonals, 
                # it must not be equal to 0, otherwise we return false.
                if i == j or (i == row and j == col):
                    if grid[i][j] == 0:
                        return False
                    
                # If we encounter a cell that is not on the diagonal and it is not equal to 0, then we also return false
                else:
                    if grid[i][j] != 0:
                        return False
            # we shift the values ​​of the variables to the next cell on the diagonal
            row += 1
            col -= 1

        return True 