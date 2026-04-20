class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        '''
        We need to find a pair of numbers that meet the problem's conditions. 
        First, we determine the first minimum number and then check the pair of numbers one by one, ensuring that neither contains 0.
        '''

        #тWe determine the first minimum number to start the search.
        a = 0
        result = []

        # We create a loop in which we iterate through all possible pairs until the variable reaches the maximum possible value.
        while a != n:
            # Let's assume the first number is 1
            a += 1

            # If a number contains 0, then it is not suitable for us and we immediately skip it and move on to the next one.
            if '0' in str(a):
                continue
            # If the first number is correct, then we find the second number using the formula
            else:
                b = n - a

            # If the second number does not contain the digit 0, then we have found a suitable pair of numbers and immediately terminate the loop.
            if '0' not in str(b):
                break
                
        result.append(a)
        result.append(b)
                
        return result