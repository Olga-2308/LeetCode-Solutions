class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        # create a loop in which we work with each number in the list
        for i in range(len(nums)):

            # create a variable for the sum of the digits of a number with a zero value, 
            # so that the sum calculation starts over again before each new number
            sum_digit = 0

            # convert the number into a string to work with each character.
            num = str(nums[i])
            
            # create a loop in which we work with each character of the string
            for n in num:

                #  each symbol is converted back into a number and added to the total sum
                sum_digit += int(n)

            # if the sum of the digits of a number is equal to the index of that number, then we return the index
            if sum_digit == i:
                return i
        
        # otherwise return -1
        else:
            return -1
        