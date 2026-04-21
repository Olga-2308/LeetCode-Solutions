class Solution:
    def minimumSum(self, num: int) -> int:
        '''
        To find the minimum sum of two numbers, you need to arrange the minimum numbers 
        in the high-order digits and the maximum numbers in the low-order digits. 
        The optimal solution is to distribute the digits of the string sequentially.
        '''

        digits = []

        # Using a loop, we create a list whose elements are easy to work with.
        for char in str(num):
            digits.append(int(char))

        # Sort the list to form an exact pair of numbers using the maximum and minimum numbers under the corresponding indices
        digits.sort() 

        # We create two strings to get exact numbers for further operations 
        # (if we initially use numbers, we will get the result of adding numbers, and not connecting symbols)
        num1 = str(digits[0]) + str(digits[2])
        num2 = str(digits[1]) + str(digits[3])

        # We find the sum of the resulting numbers
        result = int(num1) + int(num2)

        return result