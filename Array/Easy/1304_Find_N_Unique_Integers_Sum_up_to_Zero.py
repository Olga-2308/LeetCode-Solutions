
# ''' For the sum of the numbers in a list to equal zero, 
# it's clear that the sum of the positive numbers must equal the sum of the negative numbers. 

# To achieve this, you can create pairs of mirror numbers that will sum to 0, 
# regardless of how many pairs are required based on the problem statement. '''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        # create an empty list for a new array of numbers
        result = []

        # ''' If the input number is odd, there won't be enough pairs for one number. 
        # Then, you need to add 0 to ensure the array contains the exact number of numbers. '''
        if n % 2 != 0:
            result.append(0)

        # find the number of pairs of numbers that will be needed to fill the list
        middle = n // 2
        
        # ''' create a loop in which we add pairs of mirror numbers to the result one by one. 
        # start the loop with 1 so that the first pair is 1 and -1. 
        # also add 1 to the length to collect all the required pairs of numbers. '''
        for i in range(1, middle+1):
            result.append(i)
            result.append(-i)

        return result