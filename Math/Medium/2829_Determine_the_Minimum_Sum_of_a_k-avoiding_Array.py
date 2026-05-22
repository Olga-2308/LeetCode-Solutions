class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        '''
        To return the minimum sum of numbers, you need to add the smallest numbers starting with 1
        '''

        # set the first number
        number = 1

        # Let's create an empty set for faster searching, where we'll add all the new numbers
        arr = set() 

        # it is necessary to add numbers 
        # until the set contains the required number of numbers (the length of the set)
        while len(arr) < n:

            # Before adding another number, you need to check whether there is already a number in the array that, 
            # when added to the current one, is equal k 
            # We find the number using the formula
            num = k - number

            # If the found number is not in the set, then this means that we can add the current one
            if num not in arr:
                arr.add(number)
                # we increase the variable by 1 to add the next number
                number += 1

            # If the number doesn't fit, we skip it and move on to the next one.
            else:
                number += 1

        return sum(arr)