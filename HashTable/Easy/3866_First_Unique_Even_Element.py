class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        d = {}

        # we determine the frequency of each number in the array
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        # find the first even number with frequency 1 and return it
        for num in nums:
            if num % 2 == 0 and d[num] == 1:
                return num

        # If there is no such number in the array, then we return -1
        return -1