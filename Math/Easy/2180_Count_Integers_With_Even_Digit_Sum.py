class Solution:
    def countEven(self, num: int) -> int:

        # create a counter to count the number of matching numbers.
        count = 0

        # create a loop in which we check each number from the sequence from 1 (since we only need positive numbers) 
        # to num + 1 (to check the last number inclusive)
        for i in range(1, num + 1):

            # create a number variable whose value will be the current index
            number = i

            # create a variable in which we will calculate the sum of the digits of a number.
            # Before each new index (number), the sum will be reset to zero.
            sum_digits = 0

            # create a loop in which we find the sum of the digits of a number 
            # Since the number cannot be divided into parts, we turn it into a string
            for n in str(number):

                # find the sum of all the digits of a number by converting each element back 
                # to a numeric data type so that we can find their sum
                sum_digits += int(n)

            # If the sum of the digits of the number is even, then we increase the counter by 1
            if sum_digits % 2 == 0:
                count += 1

        return count