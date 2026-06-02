class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        result = []

        # We use a loop to check each suffix and prefix
        for i in range(len(nums)):

            # at each iteration we form new slices, 
            # including an index in each slice
            prefix = nums[:i+1]
            suffix = nums[i+1:]

            #We add the difference between the unique characters of the prefix and suffix, 
            # for this we transform each subarray into a set
            result.append(len(set(prefix)) - len(set(suffix)))

        return result
        