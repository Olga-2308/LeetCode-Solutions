class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        # create a loop in which we create a sequence of numbers that need to be checked
        for i in range(100):

            # Since we need to return a number equal to or greater than n, we'll check numbers from n in the loop. 
            # The index will increase the number by 1 each time, allowing us to check every option.
            number = i + n

            # create a variable that will calculate the product of the digits of a number. 
            # create the variable before the inner loop so that the variable is updated before each new number in the outer loop.
            product = 1

            # create a loop in which we check each number. 
            # Since we get a number from the outer loop, we need to convert it to a string to split it into characters.
            for num in str(number):

                # find the product of the digits of a number, 
                # first converting each character of the string into a number to perform multiplication of numbers
                product *= int(num)

            # as soon as we find a number that is divisible by t without a remainder, we return it and end the loop
            if product % t == 0:
                return number