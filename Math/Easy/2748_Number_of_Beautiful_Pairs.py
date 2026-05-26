class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:

        counter = 0

        # Using a nested loop, we check pairs of numbers; 
        # in the second loop, we make an offset of 1 so that the i < j condition is met.
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                # We turn a pair of numbers into two strings 
                # to instantly access the required digits of a number by index
                number1 = str(nums[i])
                number2 = str(nums[j])

                # If the greatest common divisor of the first digit of the first number 
                # and the last digit of the second number is 1, then we increment the counter
                if gcd(int(number1[0]), int(number2[-1])) == 1:
                    counter += 1

        return counter