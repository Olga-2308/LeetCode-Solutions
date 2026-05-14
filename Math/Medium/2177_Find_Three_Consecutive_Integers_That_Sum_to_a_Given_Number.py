class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        '''
        A number can be factored into three consecutive integers 
        whose sum is equal to that number only if that number is divisible by 3.

            Suppose n is an unknown number.
            The expression is:
        (n - 1), (n), (n + 1)  <--- +1

            It can be represented as:
        (n + 0),(n + 1),(n + 2)
        n --> (0),(1),(2), where n is the common part of all three numbers, and their remainders add up to 3. 

        Since our common part is a third of a whole number, it is divisible by 3 
        and the sum of the remainders is divisible by 3, then the whole number is divisible by 3.
        '''

        # If the number is not divisible by 3, then return false
        if num % 3 != 0:
            return []

        # otherwise, we find the common part and return the answer as required in the problem statement
        number = num // 3

        return [number - 1, number, number + 1]