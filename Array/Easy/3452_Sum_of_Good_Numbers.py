class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:

        sum_good = 0

        # using a loop, check each number and its boundaries
        for i in range(len(nums)):

            # We create a variable with which we will check whether the resulting number is suitable or not.
            good = 0

            # we define indices on both sides, the numbers of which need to be checked later
            left_indx = i - k
            right_indx = i + k

            # If there is no left index, then the condition is met and we add 1 to the variable
            if left_indx < 0:
                good += 1
            
            # if there is a boundary, and the number under the left index is less 
            # than the current one, then this is also suitable
            elif nums[i] > nums[left_indx]:
                good += 1

            # We check the right index and number in the same way
            if right_indx > len(nums) - 1:
                good += 1
            elif nums[i] > nums[right_indx]:
                good += 1

            # if the variable is equal to 2, then both the numbers (or indices) 
            # on the right and left satisfy the conditions of the problem and 
            # we add the current cycle number to the total sum
            if good == 2:
                sum_good += nums[i]

        return sum_good