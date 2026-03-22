class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # create a variable to count the product of the digits of a number
        product = 1
        # create a variable to calculate the sum of the digits of a number
        sum = 0

        # create a loop to process the digits of a number
        while n > 0:
            # find the last digit of a number
            dig = n % 10
            # perform the multiplication action
            product *= dig
            # perform the addition action
            sum += dig
            # remove the last digit of a number
            n //= 10

        result = product - sum
        return result