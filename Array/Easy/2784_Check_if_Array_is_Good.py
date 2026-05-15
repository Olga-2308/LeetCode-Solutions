class Solution:
    def isGood(self, nums: List[int]) -> bool:

        n = max(nums)
        l = len(nums)

        # An array is bad if its length is not equal to the maximum value plus 1, 
        # since the maximum value must appear in the array twice.
        if n + 1 != l:
            return False

        # If there are no two identical maximum elements in an array, then the array is bad
        if nums.count(n) != 2:
            return False

        # in other cases, if all elements in the array are unique except for the maximum 
        # (of which there should be two), then the array is good
        num = set(nums)
        if len(num) == n:
            return True

        # If there are fewer unique elements in a set, 
        # then there are more duplicates in the array and the array is bad
        return False