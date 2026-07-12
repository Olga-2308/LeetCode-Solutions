class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:

        '''
        We need to find at least two numbers whose bitwise operation OR results in at least one 0 at the end. 
        For the bitwise operation OR to result in 0, two values ​​of the two numbers must also be 0 in their bitwise representation. 
        If a number's bitwise representation ends in 0, it means the number is even, 
        since dividing a decimal number by 2 yields 0, which is the final bit of that number in binary form.
        '''

        counter = 0

        for num in nums:
            if num % 2 == 0:
                counter += 1

        return counter >= 2
        