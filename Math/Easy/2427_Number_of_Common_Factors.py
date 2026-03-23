class Solution:
    def commonFactors(self, a: int, b: int) -> int:

        # create a counter for counting numbers
        counter = 0

        # ''' We find the smallest number. 
        # This is necessary to determine how many loop iterations are needed. 
        # It is obvious that the number of possible divisors will not exceed the minimum number. '''
        min_num = min(a, b)

        # ''' We create a loop in which we check each number from the minimum number. 
        # Since we need to check numbers starting with 1, we start the loop with 1, 
        # and to check the last number, we need to add 1 to the end. '''
        for i in range(1, min_num+1):

            # ''' If the number is simultaneously a divisor (without remainder) for the input numbers, 
            # then the condition is met and the counter is incremented. '''
            if a % i == 0 and b % i == 0:
                counter += 1
        
        return counter