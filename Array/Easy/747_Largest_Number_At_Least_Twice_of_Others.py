class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        '''
        We find the unique maximum value in the array, with which we need to compare the obtained results in the future.
        '''
        max_number = max(nums)

        '''
        We create a loop in which we check each number. 
        Since this array also contains the maximum number found, 
        as soon as this number appears in the loop, all operations with it must be skipped, 
        otherwise an incorrect result will be obtained. 
        If the remaining numbers in the array, when multiplied by 2, 
        do not exceed the maximum number in the array, then all the conditions of the problem are met.
        '''
        for num in nums:
            if num == max_number:
                continue
            elif num * 2 > max_number:
                return -1

        '''
        We return the index of the maximum number, as required in the problem statement.
        '''
        return nums.index(max_number)