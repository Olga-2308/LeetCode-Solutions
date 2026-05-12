class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        # we create a result variable with the value -1 in case a matching pair of numbers is not found
        result = -1

        # we set the minimum value, which is defined as the first element of the array
        min_value = nums[0]

        # Using a loop, we find the difference between matching pairs of numbers one by one 
        # and update the minimum value of the variable if it appears in the array
        for i in range(1, len(nums)):
            if nums[i] < min_value:
                min_value = nums[i]
            elif nums[i] > min_value:
                diff = nums[i] - min_value

                # If the current difference is greater than the one found previously, 
                # then we update the result variable
                if diff > result:
                    result = diff

        return result