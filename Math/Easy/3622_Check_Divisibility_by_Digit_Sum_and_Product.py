class Solution:
    def checkDivisibility(self, n: int) -> bool:

        # we create a list in which we will enter individual digits from the number
        digits = []

        # We create a variable to calculate the product of the digits of a number, 
        # and specify 1 so that the product is not equal to 0.
        product = 1

        # We create a loop in which we work with each digit. 
        # Since we are given a number, we convert it to a string so that we can separate each element.
        for num in str(n):

            # First we add the resulting number to the list (we convert the string symbol back into a number)
            digits.append(int(num))

            # then we find the common product of all digits of the number (we convert the string symbol back into a number)
            product *= int(num)

        # we find the divisor as indicated in the problem statement
        divisor = product + sum(digits)

        # If the number is divisible by the resulting divisor without a remainder, then return true, otherwise false
        return n % divisor == 0