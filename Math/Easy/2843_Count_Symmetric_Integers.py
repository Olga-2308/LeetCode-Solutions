class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        # create a counter to count the number of symmetric numbers
        counter = 0

        # create a loop and check all numbers in a given range
        for num in range(low, high + 1):

            # convert a number to a string to split the string in half
            s = str(num)

            # find the length of the string to determine the midpoint
            l = len(s)

            # create variables to calculate the sum of the digits in each number; 
            # before each new number, the current sums are reset to zero.
            left_sum = 0
            right_sum = 0

            # If a number consists of an odd number of digits (a string of an odd number of elements), 
            # then this number is skipped
            if l % 2 != 0:
                continue

            # find the center of the line
            middle = l // 2
                
            # create two slices with the same number of characters
            left = s[:middle]
            right = s[middle:]

            # find the sum of the digits on the left, turning each symbol into a number
            for char in left:
                left_sum += int(char)

            # find the sum of the digits on the right, turning each symbol into a number
            for char in right:
                right_sum += int(char)

            # If the sums of the two parts are equal, increase the counter by 1
            if left_sum == right_sum:
                counter += 1
             
        return counter