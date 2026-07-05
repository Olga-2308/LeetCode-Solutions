class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:

        # we create two variables, where one contains the current maximum rank, 
        # and the second calculates the total sum of the corresponding rank
        max_range = -1
        total_sum = 0

        # Using a loop, we find the rank for each number. 
        # First, we sort the characters in the string 
        # and find the difference between the highest and lowest digits.
        for num in nums:
            number = sorted(str(num))
            r = int(number[-1]) - int(number[0])

            # If the new rank is greater than the current one, 
            # we update the rank value and reset the sum, since it is no longer suitable, 
            # and add the new value to the total sum.
            if r > max_range:
                max_range = r
                total_sum = 0
                total_sum += num

            # If the new rank is the same as the current rank, 
            # then we continue to accumulate the sum, 
            # since there is no higher rank or it has not yet been found
            elif r == max_range:
                total_sum += num

        return total_sum