class Solution:
    def isThree(self, n: int) -> bool:

        # We create a counter for counting divisors
        counter = 0

        # ''' We create a loop with a range of numbers from 1 to the last number and check whether the number satisfies the condition. 
        # If the condition is met, we add 1 to the counter. '''
        for i in range(1, n+1):
            if n % i == 0:
                counter += 1

        # If the counter is 3, return true, otherwise return false.
        if counter == 3:
            return True
        else:
            return False