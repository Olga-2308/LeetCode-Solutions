class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        # create an empty list to add suitable numbers
        result = []

        # We create a loop in which we create a range of numbers to be checked. 
        # The bounds are specified in the problem statement; 
        # we add 1 to the right bound so that the last number also passes the loop iteration.
        for i in range(left, right + 1):

            # create a variable for the current number
            num = i

            # We create a loop in which we check each number for compliance with the conditions of the problem.
            # Since we need to check each digit of the number individually, we convert the number into a string.
            for digit in str(num):

                # We check that the digit of the number is not equal to zero and that the number is divisible by the digit without a remainder. 
                # Since the loop uses a string character, we convert this character to a number so that arithmetic operations can be used.
                if int(digit) == 0 or i % int(digit) != 0:
                    break

            # If after checking all the digits of a number, these digits meet the conditions, 
            # then we add the number to the list, and the outer loop moves on to the next one
            else:
                result.append(i)

        return result