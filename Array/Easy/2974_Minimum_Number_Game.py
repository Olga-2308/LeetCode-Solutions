class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

# The problem description states that Alice and Bob alternately select the smallest number from a list. 
# Once they've each selected a number, they write their empty list in reverse order. 
# This means the numbers are swapped in pairs each time. 
# Since the list contains pairs of elements, we can immediately loop through the sorted pairs of numbers.

        # create a new list to record the result
        arr = []

        # sort the list
        nums.sort()

        # We create a loop in which we will work with each pair of numbers. 
        # To do this, we set the start to 0, and the end to the length of the list to 1 
        # (to avoid going beyond the bounds, in the last iteration we will work with the last pair of numbers i and i +1. 
        # We set the step to 2 to work with each pair independently of each other).
        for i in range(0, len(nums)-1, 2):

            # swap a couple of numbers
            nums[i], nums[i+1] = nums[i+1], nums[i]

            # we add numbers to the list sequentially
            arr.append(nums[i])
            arr.append(nums[i+1])

        return arr


        