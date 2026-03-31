class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        # create a variable to find the sum of squares of numbers
        result = 0

        # find the length of the list
        n = len(nums)

        # create a loop in which we work with each number in order
        for i in range(n):

            # Since in the problem statement indexing starts from 1, and in the loop the first number is under index 0, 
            # it is necessary to update the index to 1
            indx = i + 1

            # if the length of the list is divisible by the updated index without remainder:
            if n % indx == 0:

                # find the square of a number
                num = nums[i] ** 2

                # add the square of the number to the total result
                result += num

        return result