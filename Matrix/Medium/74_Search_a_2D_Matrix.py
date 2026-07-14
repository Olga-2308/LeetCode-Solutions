class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        # Since the matrix is ​​sorted, we check its first element and if it is greater than the given number, 
        # then the matrix itself does not contain the given number, and we immediately return false
        if matrix[0][0] > target:
            return False

        # We also return false if the last element of the matrix is ​​less than the given one, 
        # since all numbers before the last element are less than the given one.
        if matrix[row-1][col-1] < target:
            return False

        # create a nested loop
        for i in range(row):

            # in the outer loop, at each iteration, you can check the last element of the string, 
            # and if it is less than the specified number, then the current string cannot contain the desired number, 
            # and we skip it
            if target > matrix[i][col-1]:
                continue

            # Once we have found a suitable string, we use the inner loop to check the elements in search 
            # of the given number and return true if such a number was found.
            for j in range(col):
                if matrix[i][j] == target:
                    return True

            # If the number was not found in the current line, then we return false, 
            # since further searching does not make sense - 
            # all subsequent numbers are guaranteed to be greater than the specified one
            return False