class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        '''
        Using a nested loop, we find pairs of numbers 
        that match the conditions of the problem
        '''

        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) >= valueDifference and abs(i - j) >= indexDifference:
                    return [i, j]
                
        return [-1, -1]