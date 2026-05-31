class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:

        counter = 0

        # Using a triple loop, we find matching triplets. 
        # To avoid repeating indices, we shift the start by 1 from the previous loop.
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):

                    # As soon as we find three suitable values, we increase the counter by 1
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        counter += 1

        return counter