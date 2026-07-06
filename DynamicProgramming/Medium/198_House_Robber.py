class Solution:
    def rob(self, nums: List[int]) -> int:

        l = len(nums)

        # If there is only one house on the street, then you can only rob it
        if l == 1: 
            return nums[0]
        
        # If there are only 2 houses on the street, then you can only rob one, 
        # and we choose the one with the higher number
        elif l == 2:
            return max(nums)

        # we create a dynamic array equal to the length of the given array
        dp = [0] * l

        # on the first number, only this number can be selected
        dp[0] = nums[0]

        # on the second number we select the maximum value between the current and the previous one
        dp[1] = max(nums[0], nums[1])

        # Next, using a loop, we determine the maximum number for each subsequent number, 
        # starting from the second index (third house)
        for i in range(2, l):

            # Since you can't rob two neighboring houses, 
            # you need to determine each time where there will be more money: 
            # if you rob the previous house, or rob the current house and the one next to the left, 
            # and write down the potentially largest number
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1] 