class Solution:
    def maxProduct(self, n: int) -> int:

        # To find the maximum product among a set of numbers, it is necessary to determine the two maximum numbers and, 
        # therefore, the result of their product will also be the maximum

        # Since a number is given, it is necessary to create a list in order to add and divide the digits from the number
        digits = []

        # We'll create a loop in which we'll add each digit to the list one by one. 
        # Since a number can't be divided into digits, we'll convert the number into a string. 
        # We'll then add each element to the list.
        for num in str(n):
            digits.append(int(num))

        # To easily determine the two maximum numbers, you need to sort the list in descending order 
        # (you can sort it in ascending order by default, then you need to use the indices -1 and -2)
        digits.sort(reverse = True)

        # we return the product of the two maximum digits from the list under indices 0 and 1
        return digits[0] * digits[1]