class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # create an empty list to record the results
        result = []

        # create a variable for the current sum of numbers
        current_sum = 0

        # create a loop in which we work with each number in order
        for num in nums:

            # add the number to the current sum
            current_sum += num

            # add the obtained result to the list
            result.append(current_sum)

        return result