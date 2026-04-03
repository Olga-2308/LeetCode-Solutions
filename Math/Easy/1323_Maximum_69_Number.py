class Solution:
    def maximum69Number (self, num: int) -> int:

        # To get the largest possible number in one step, you need to change the most significant digit

        # convert the number into a string so that we can work with the characters individually.
        n = str(num)

        # turn the string into a list of characters so that we can change these characters.
        numbers = list(n)

        # create a loop in which we check each character
        for i in range(len(numbers)):

            # if the first value is 6
            if numbers[i] == '6':

                # This means we replace it with 9 and get the maximum number in 1 change 
                # (if, for example, the first digit is 9, then we check the next digit of the number)
                numbers[i] = '9'

                # As soon as we have replaced one found digit, we stop the loop, 
                # since according to the problem statement, only one replacement is possible
                break

        # converting the list back to a string
        res = ''.join(numbers)

        # convert the string into a number, as required by the problem statement
        result = int(res)

        return result