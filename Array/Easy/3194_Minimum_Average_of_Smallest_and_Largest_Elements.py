class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        # create an empty list to add average values
        averages = []

        # We sort the list to easily remove the first and last elements of the list by index (0) and (-1) respectively.
        nums.sort()

        # find the number of steps (specified in the problem statement)
        moves = len(nums) / 2

        # create a loop that runs until there are no more moves
        while moves != 0:

            # find the minimum and maximum values ​​in the list
            minElement = min(nums)
            maxElement = max(nums)

            # find the average value of a pair of numbers and add it to the list.
            aver = (minElement + maxElement) / 2
            averages.append(aver)

            # remove the first and last elements of the list, which are the minimum and maximum values
            nums.pop(0)
            nums.pop(-1)

            # reduce the number of steps by 1 to avoid getting stuck in an infinite loop.
            moves -= 1

        # find the minimum value in the list
        result = min(averages) 

        return result

    # aver = (nums[-1] + nums[0]) / 2 -- a faster way