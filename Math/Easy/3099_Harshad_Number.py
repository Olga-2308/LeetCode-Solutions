class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        # create a copy of the number to work with it in the loop
        cop_x = x

        # create a variable to calculate the sum of the digits of a number
        sum = 0

        # create a loop and find the sum of all the digits of a number
        while cop_x > 0:
            # find the last digit of the number
            dig = cop_x % 10
            # add a digit to the sum variable
            sum += dig
            # delete the last digit
            cop_x //= 10

        # check the condition, if it is met, we return the sum of the digits of the number, otherwise we return -1
        if x % sum == 0:
            return sum
        else:
            return -1