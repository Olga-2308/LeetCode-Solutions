class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        # We create a counter to count the number of operations
        counter = 0

        # ''' We create a loop that will run until one of the numbers becomes equal to 0 
        # (we use the AND operator - as soon as one number becomes 0, the loop ends) '''
        while num1 > 0 and num2 > 0:

            # If num1 is greater than or equal to num2, then we subtract num2 from num1 and increase the counter by 1
            if num1 >= num2:
                num1 = num1 - num2
                counter += 1
            
            # Otherwise we subtract num1 from num2 and increase the counter by 1
            else:
                num2 = num2 - num1
                counter += 1

        return counter

        