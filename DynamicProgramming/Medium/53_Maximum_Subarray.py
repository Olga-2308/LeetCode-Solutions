class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        l = len(nums)

        # If the length of the array is 1, 
        # then the maximum sum is always equal to the value of a single element
        if l == 1:
            return nums[0]

        # create a dynamic array the length of the original array
        dp = [0] * l

        # we define the first element as the value of the first element, 
        # since with a length of 1 element this sum is maximum
        dp[0] = nums[0]

        # using a loop, we determine all possible maximum sums of the elements of the subarray at each iteration, 
        # starting from index 1 (the second element)
        for i in range(1, len(nums)):

            # It is necessary to determine the maximum sum that can be obtained for a given element. 
            # This can be either the value of the element itself, 
            # or the sum of the current element with all possible sums of the previous element in the dynamic array.
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        # return the maximum value that was found
        return max(dp)