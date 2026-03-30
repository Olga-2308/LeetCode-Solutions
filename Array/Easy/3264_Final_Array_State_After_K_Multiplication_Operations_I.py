class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        # create a loop that runs until the number of operations k becomes equal to 0
        while k != 0:

            # find the minimum value from the list
            min_num = min(nums)

            # find the index of this minimum number
            indx = nums.index(min_num)

            # replace this number with the value multiplied by the multiplier
            nums[indx] = min_num * multiplier

            # reduce the number of operations by 1 to avoid creating an infinite loop.
            k -= 1

        return nums