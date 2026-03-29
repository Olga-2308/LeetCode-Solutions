class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:

        # create a loop in which we work with each number
        for i in range(len(nums)):

            # If the number is even, then we replace it with 0
            if nums[i] % 2 == 0:
                nums[i] = 0

            # otherwise we replace the number with 1
            else:
                nums[i] = 1

        # sort the resulting list in ascending order
        nums.sort()

        return nums