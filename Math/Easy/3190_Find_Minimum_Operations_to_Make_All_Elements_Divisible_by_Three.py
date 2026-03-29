class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        # If a number is divisible by ri without a remainder, then we don't work with this number in the loop. 

        # If a number is divisible by three with only a remainder, then we can get either 1 or 2 as a remainder. 

        # It turns out that in order to ultimately obtain the required number, it is necessary to subtract this 1 from the number once, 
        # and then the division will be without a remainder. And if the remainder is 2, 
        # then it is necessary to add 1 so that there is no remainder when dividing the number by 3. 
        
        # Therefore, for any number to be divisible by 3 without a remainder, it is necessary to add 1 to this number or, 
        # conversely, subtract 1. It turns out that if a number is not divisible without a remainder, 
        # then one operation is required to fulfill the condition. 
        
        # It is simply necessary to find the number of numbers that, when divided by 3, are not equal to 0, but leave a remainder.

        # create a counter to count operations
        counter = 0

        # create a loop in which we iterate over all the numbers from the list in order.
        for num in nums:

            # If the number is not divisible by 3 without a remainder, then we increase the counter by one
            if num % 3 != 0:
                counter += 1

        return counter 