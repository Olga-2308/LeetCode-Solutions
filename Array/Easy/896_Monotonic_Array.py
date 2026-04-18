class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        '''
        To determine whether an array of numbers is an increasing or decreasing sequence, 
        it is necessary to create sample sequences and compare them with the original
        '''
        increasing = nums.copy()
        decreasing = nums.copy()

        '''
        Sort copies of arrays to get two sequences of numbers
        '''
        increasing.sort()
        decreasing.sort(reverse = True)

        '''
        If the original array is equal to one of the sequences, then return true, otherwise false.
        '''
        return increasing == nums or decreasing == nums