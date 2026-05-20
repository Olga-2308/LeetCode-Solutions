class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        d = {}

        # we determine the frequency of each number in the array
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        # We check each frequency in the dictionary.
        for freq in d.values():

            # If the frequency is greater than 2, 
            # it means that the same numbers cannot be distributed across two arrays 
            # so that this number is unique in each array.
            if freq > 2:
                return False

        # if all frequencies are less than or equal to 2, 
        # then the arrays can be composed and we return true
        return True