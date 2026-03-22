class Solution:
    def countDigits(self, num: int) -> int:

        # create a copy of the number we will work with in the loop
        cop_num = num

        # create a counter to count the number of digits that fulfill the conditions of the loop
        counter = 0

        # create a loop in which we work with a new number (cop_num)
        while cop_num > 0:
            # find the last digit of the number
            val = cop_num % 10
            # if the original number (num) is divisible by the last digit (val), then the condition is satisfied
            if num % val == 0:
                # add 1 to the counter
                counter += 1
            # remove the last digit from the number (cop_num) and start the next cycle with a new number
            cop_num //= 10

        return counter
        