class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = []

        # Using a loop, we fill the new array with numbers one by one.
        for i in range(n):

            # If the current number is 0, then we also add 0 to the final array.
            if nums[i] == 0:
                result.append(nums[i])

            # in this case, it is possible to shift the index to the right or to the left, 
            # depending on whether the number is positive or negative
            else:

                # We define a new index whose number will be added to the resulting array. 
                # Using the remainder of the integer division, 
                # we determine the positive index we need, 
                # regardless of whether the number is positive or negative. 
                # The result will always be a positive index.
                indx = (i + nums[i]) % n

                # add the found number to the result
                result.append(nums[indx])

        return result 