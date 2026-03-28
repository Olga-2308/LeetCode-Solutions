class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        # We create a counter to count the number of numbers that contain an even number of digits.
        counter = 0

        # we create a loop in which we iterate over each number in order
        for num in nums:

            # convert a number to a string to count the number of characters
            s = str(num)

            # we find the length of the string, which is the number of characters in the string
            l = len(s)

            # If the number of digits is divisible by 2 without a remainder, then the number is even and we increase the counter by 1
            if l % 2 == 0:
                counter += 1

        return counter