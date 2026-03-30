class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        # create a list for the sum of the digits of each number
        result = []

        # we create a loop in which we work with each number
        for num in nums:

            # We set the current sum of the digits of the number, 
            # and set a variable before the second loop so that the result is reset to zero for the new number.
            total = 0

            # We create a loop in which we work with each number from the list separately, 
            # and immediately convert this number into a string so that we can work with the symbols of the number separately, 
            # since it is impossible to divide the number into individual digits.
            for digit in str(num):

                # we find the sum of the digits of a number
                total += int(digit)

            # add the sum of the digits of one number to the list
            result.append(total)

        # return the minimum value from the list
        return min(result)