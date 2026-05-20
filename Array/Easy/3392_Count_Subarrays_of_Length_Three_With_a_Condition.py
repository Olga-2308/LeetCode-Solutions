class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        counter = 0

        # We use a loop to check each subarray 
        # (starting with 1 to check the previous element 
        # and working our way up to the penultimate index 
        # to avoid going beyond the loop boundary)
        for i in range(1, len(nums) - 1):

            # if equality is satisfied, then we increase the counter
            if 2 * (nums[i-1] + nums[i+1]) == nums[i]:
                counter += 1

        return counter