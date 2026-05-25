class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        d = {}

        # We write all the unique numbers from the array into a dictionary 
        # and assign each one a counter with the value 0
        for num in nums:
            if num not in d:
                d[num] = 0

        # We check each subarray in the array to make sure we don't go beyond the loop boundary, 
        # subtract the length of the desired array, and add 1 to check the last element.
        for i in range(len(nums) - k + 1):

            # we define an array lenght k
            subarray = nums[i:i+k]

            # We convert the array into a set to remove duplicates, 
            # since if numbers are repeated in one subarray, they are counted as 1 occurrence
            unique_subarray = set(subarray)

            # We determine the number of occurrences of each number in each subarray and count their total number
            for num in unique_subarray:
                d[num] += 1

        result = -1

        # We determine the number that occurs only once, 
        # and if there are several such numbers, we return the maximum of them.
        for num, freq in d.items():
            if freq == 1:
                result = max(result, num)

        return result