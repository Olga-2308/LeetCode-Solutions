class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:

        counter = 0

        # We check each number using a loop
        for num in nums:

            # We check each digit of the number by converting the number into a string 
            # to check the characters individually.
            for char in str(num):

                # we count the number of required digits
                if char == str(digit):
                    counter += 1

        return counter