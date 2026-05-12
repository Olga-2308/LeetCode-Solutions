class Solution:
    def dominantIndices(self, nums: List[int]) -> int:

        counter = 0

        # we find the length of the array, which will be updated for each new iteration
        l = len(nums)

        # we determine the total sum of all elements of the array
        total = sum(nums)

        # using a loop, we check all the indices one by one, except for the rightmost one (-1)
        for i in range(len(nums) - 1):

            # The current number must be subtracted from the total sum, 
            # since it is with this number that the average value will be compared
            total -= nums[i]

            # accordingly, the length of the array also decreased
            l -= 1

            # If the current value is greater than the arithmetic mean of all numbers on the right side, 
            # this means that the index is dominant and we increase the counter by 1
            if nums[i] > (total / l):
                counter += 1

        return counter