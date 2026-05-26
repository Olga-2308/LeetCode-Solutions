class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        '''
        using the method we unfold the array of numbers and 
        return the total array consisting of the array in direct order and the unfolded array
        '''

        return nums + nums[::-1]