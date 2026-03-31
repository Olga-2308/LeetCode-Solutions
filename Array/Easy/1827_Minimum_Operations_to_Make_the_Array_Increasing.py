class Solution:
    def minOperations(self, nums: List[int]) -> int:

    # The problem requires creating an ascending sequence of numbers in a list using a minimum number of steps. 
    # To minimize the number of steps, each successive number must be equal to the previous one and increased by one. 
    # The difference between two adjacent numbers and 1 will be the required number of steps at each stage of the cycle.

        # create a variable to count the total number of increases by 1
        total = 0

        # create a variable that will increase the next number by 1 from the current one
        step = 1

        # create a loop in which we check each number, 
        # reaching the second-to-last number (length - 1) to avoid going beyond the bounds. 
        # The second-to-last number is compared with the last one, and the loop ends.
        for i in range(len(nums)-1):

            # if the current number is greater than or equal to the next number
            if nums[i] >= nums[i+1]:

                # find the difference between the numbers, which is the number of steps to align two adjacent numbers
                num = nums[i] - nums[i+1]

                # write down this difference in numbers in the total number and one more step so that the sequence is increasing
                total += (num + step)

                # write down the new value of the next number, 
                # which is now 1 unit greater than the previous one, 
                # which corresponds to the condition of an increasing sequence of numbers
                nums[i+1] = nums[i] + step
                
        return total