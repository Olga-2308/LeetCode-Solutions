class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        # we find a number that is the frequency of an element in the list
        n = len(nums) // 2

        # create a loop in which we check each number
        for num in nums:

            # If we find a number that appears in the list n times, then we immediately return that number
            if nums.count(num) == n:
                return num