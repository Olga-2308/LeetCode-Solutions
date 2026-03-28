class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # create an empty list for squares of numbers
        squares = [] 

        # create a loop in which we work with each number
        for num in nums:

            # we square a number
            n = num ** 2

            # add the square of the number to the final list
            squares.append(n)

        # sort the list in ascending order (from smallest to largest)
        squares.sort() 

        return squares