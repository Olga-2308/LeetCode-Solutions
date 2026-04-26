class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # We create a set based on a given list. This is necessary to check for duplicates in the list.
        s_nums = set(nums)

        # If the length of the list and the length of the set are equal, 
        # this means that every element of the list was added to the set and each of the nick is unique 
        # (otherwise, a duplicate element in the list would not be re-added to the set, 
        # and then the lengths of the list and the set would become different)
        if len(nums) == len(s_nums):
            return False
        else:
            return True