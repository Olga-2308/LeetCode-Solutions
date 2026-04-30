class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        # We find the length of the original array to find out the number of loop iterations
        l = len(nums)

        for i in range(0, l):

            # The current loop number is converted into a string to expand the characters
            n = str(nums[i])
            num = n[::-1]

            # We add the resulting value to the array, having first converted the string back into a reversed number.
            nums.append(int(num))

        # Converting a list to a set to remove all duplicates
        result = set(nums)

        # Return the number of unique characters
        return len(result)