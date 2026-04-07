class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        
        # To get the maximum value of an expression, 
        # you need to find the sum of the two maximum numbers and subtract the minimum number from it

        # We sort a list of numbers to easily determine the maximum and minimum numbers in the array.
        nums.sort()

        #  We add the two largest numbers, which are on the right side of the sorted list under indexes -1 and -2, 
        # and subtract from the sum the smallest number, which is at the beginning of the list under index 0
        result = (nums[-1] + nums[-2]) - nums[0]

        return result