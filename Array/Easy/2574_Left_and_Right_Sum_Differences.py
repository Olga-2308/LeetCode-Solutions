class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        # create an empty list for the final result
        result = []

        # ''' create two empty lists into which we will add the accumulated sums of numbers one by one 
        # (a list for the sum on the right and a list for the sum on the left) '''
        leftSum = []
        rightSum = []

        # create variables in which we will store the accumulated amount
        pre_leftSum = 0
        pre_rightSum = 0

        # create a loop to calculate the sum of numbers leftSum
        for i in range(len(nums)):
            # add a number to the list for amounts leftSum
            leftSum.append(pre_leftSum)
            # add the current cycle number
            pre_leftSum += nums[i]

        # reverse the input list to calculate the sums of the numbers in reverse order.
        nums_rev = nums[::-1]

        # create a loop to calculate the sum of numbers rightSum
        for i in range(len(nums_rev)):
            rightSum.append(pre_rightSum)
            pre_rightSum += nums_rev[i]

        # reverse the list of the resulting sums back so that the numbers are in the correct order for further calculations
        rightSum = rightSum[::-1]

        # create a loop to calculate the difference in the absolute values ​​of two parallel numbers.
        for i in range(len(nums)):
            answer = abs(leftSum[i] - rightSum[i])
            # add the resulting number to the result
            result.append(answer)

        return result