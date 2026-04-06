class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        # create a variable into which we will write the XOR maximum value
        result = 0

        # create a nested loop to check and find pairs that match the problem conditions.
        for i in range(len(nums)):
            for j in range(len(nums)):

                # If the absolute value of the difference between two paired numbers is less than or equal to the minimum value of this pair, 
                # then the pair of numbers is considered strong
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):

                    # find the XOR value between the numbers in a pair
                    pair = nums[i] ^ nums[j]

                    # If the resulting value is greater than the value in the variable, the result is assigned a new value
                    if pair > result:
                        result = pair

        return result