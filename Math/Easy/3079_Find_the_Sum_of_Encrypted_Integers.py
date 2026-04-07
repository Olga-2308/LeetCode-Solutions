class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:

        # create a variable in which we will calculate the sum of the new numbers
        result = 0

        # create a loop in which we transform each number from the array.
        for num in nums:
            
            # convert a number into a string so that we can work with individual digits of the number.
            n = str(num)

            # find the maximum digit of the number. This is what the new number will consist of.
            max_dig = max(n)

            # create a new number equal to the previous one in length and with the maximum digit from the same number
            new_num = max_dig * len(n)

            # add the resulting number to the total sum
            result += int(new_num)
            
        return result