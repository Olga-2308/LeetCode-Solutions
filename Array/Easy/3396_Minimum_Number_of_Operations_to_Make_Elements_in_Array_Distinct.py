class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        operations = 0

        # We remove triplets of numbers from the beginning of the array one by one 
        # until the length of the array is equal to the length of the set 
        # (in this case, only unique elements remain in the array)
        while len(set(nums)) != len(nums):

            nums = nums[3:]
            operations += 1

        return operations