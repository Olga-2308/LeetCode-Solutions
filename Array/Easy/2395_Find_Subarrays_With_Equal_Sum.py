class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:

        d = {}

        # We use a loop to check pairs of numbers
        for i in range(len(nums) - 1):

            # we find the sum of adjacent numbers
            num = nums[i] + nums[i+1]

            # If the resulting number is not in the dictionary, then we add its value
            if num not in d:
                d[num] = 1

            # If such a value is in the dictionary, 
            # then there are two pairs of numbers in the array 
            # that match the condition, and we return true
            else:
                return True

        return False