class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        Using a sliding window, we calculate the sum of each window of size k 
        and determine the maximum value
        '''

        # If the array length is less than the window size, then return 0
        if len(nums) < k:
            return 0

        # we find the sum of the values ​​of the first window and set it as the maximum
        current = sum(nums[:k])
        max_sub = current

        # using a loop, we move each iteration one step forward and calculate the sum of the values ​​in a new window
        for i in range(k, len(nums)):
            current = current + nums[i] - nums[i-k]

            # we find the maximum value
            max_sub = max(max_sub, current)

        # In the problem statement, it is necessary to find the average value, 
        # since the maximum average value will be obtained from the maximum sum of elements, 
        # then in the loop you can find only the sum of the window, 
        # and at the end return the average value of the maximum sum found
        return max_sub / k